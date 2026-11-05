#!/usr/bin/env julia
# Приложение C. Шесть корректных графиков на Julia.
# Запуск:
#   JULIA_DEPOT_PATH="$PWD/.julia:$HOME/.julia" \
#   julia --project=09_appendices/julia_env 09_appendices/julia/six_plots.jl

using Plots, DataFrames, CSV, Statistics, Random
ENV["GKSwstype"] = "100"
Random.seed!(20240616)

root = normpath(joinpath(@__DIR__, "..", ".."))
df = CSV.read(joinpath(root, "data", "09_appendix_dataset.csv"), DataFrame)
groups = ["Контроль", "Препарат A", "Препарат B"]
colors = Dict("Контроль" => "#7F7F7F", "Препарат A" => "#0072B2", "Препарат B" => "#D55E00")

default(
    fontfamily = "sans-serif",
    guidefontsize = 8,
    tickfontsize = 6,
    titlefontsize = 8,
    legendfontsize = 6,
    legend = :bottom,
    framestyle = :axes,
    grid = true,
    gridalpha = 0.12,
    minorgrid = false,
    margin = 2Plots.mm,
)

agg = combine(
    groupby(df, [:group, :week]),
    :sbp_mm_hg => mean => :mean,
    :sbp_mm_hg => std => :sd,
    :sbp_mm_hg => length => :n,
)
agg.ci = 1.96 .* agg.sd ./ sqrt.(agg.n)

p1 = plot(title = "A. САД по неделям", xlabel = "Неделя", ylabel = "САД, мм рт. ст.")
for g in groups
    s = filter(:group => ==(g), agg)
    plot!(p1, s.week, s.mean, ribbon = s.ci, fillalpha = 0.15,
          linecolor = colors[g], markercolor = colors[g], label = g,
          marker = :circle, ms = 2, lw = 1)
end

patients = unique(df, :patient_id)
p2 = plot(title = "B. BMI и глюкоза", xlabel = "BMI, кг/м²", ylabel = "Глюкоза, ммоль/л")
for g in groups
    s = filter(:group => ==(g), patients)
    scatter!(p2, s.bmi_kg_m2, s.glucose_mmol_l, markercolor = colors[g],
             markerstrokecolor = colors[g], alpha = 0.45, ms = 2, label = g)
end

wide = unstack(df, [:patient_id, :group], :week, :sbp_mm_hg)
wide.change = wide[!, "12"] .- wide[!, "0"]
p3 = plot(title = "C. Δ САД к 12-й неделе", ylabel = "Δ САД, мм", xticks = (1:3, groups), legend = false)
for (i, g) in enumerate(groups)
    vals = filter(:group => ==(g), wide).change
    scatter!(p3, fill(i, length(vals)) .+ randn(length(vals)) .* 0.06, vals,
             markercolor = colors[g], markerstrokecolor = colors[g],
             alpha = 0.4, ms = 1.6, label = "")
    med = median(vals)
    plot!(p3, [i - 0.22, i + 0.22], [med, med], color = "#333333", lw = 1.4)
end
hline!(p3, [0], color = "#777777", ls = :dash, lw = 0.6)

chg = combine(groupby(wide, :group), :change => mean => :mean, :change => std => :sd, :change => length => :n)
chg.ci = 1.96 .* chg.sd ./ sqrt.(chg.n)
p4 = bar(groups, chg.mean, yerror = chg.ci, color = [colors[g] for g in groups],
         title = "D. Среднее Δ и 95 % ДИ", ylabel = "Δ САД, мм", legend = false)
hline!(p4, [0], color = "#777777", lw = 0.6)

mat = zeros(3, 4)
for (i, g) in enumerate(groups), (j, w) in enumerate([0, 4, 8, 12])
    mat[i, j] = filter(r -> r.group == g && r.week == w, df).sbp_mm_hg[1] |> x -> x
end
# средние по группе и неделе
for (i, g) in enumerate(groups), (j, w) in enumerate([0, 4, 8, 12])
    mat[i, j] = mean(filter(r -> r.group == g && r.week == w, df).sbp_mm_hg)
end
p5 = heatmap([0, 4, 8, 12], 1:3, mat, color = :viridis, yflip = true,
             yticks = (1:3, groups), title = "E. САД: группа × неделя",
             xlabel = "Неделя", colorbar_title = "мм")
for i in 1:3, j in 1:4
    annotate!(p5, [0, 4, 8, 12][j], i, text(round(Int, mat[i, j]), 5.5, :white))
end

p6 = plot(title = "F. Выживаемость (KM)", xlabel = "Месяцы", ylabel = "Выживаемость",
          ylim = (0, 1), legend = :bottom)
for g in groups
    s = sort(filter(:group => ==(g), patients), :time_months)
    ts = unique(s.time_months)
    xs, ys = [0.0], [1.0]
    surv, atrisk = 1.0, nrow(s)
    for t in ts
        d = sum((s.time_months .== t) .& (s.event .== 1))
        c = sum((s.time_months .== t) .& (s.event .== 0))
        if d > 0
            surv *= 1 - d / atrisk
            push!(xs, t); push!(ys, surv)
        end
        atrisk -= d + c
    end
    plot!(p6, xs, ys, seriestype = :steppost, linecolor = colors[g], lw = 1, label = g)
end

out = joinpath(root, "images", "09_julia_six.png")
plot(p1, p2, p3, p4, p5, p6, layout = (2, 3), size = (1800, 1200), dpi = 300)
savefig(out)
println("saved: ", out)
