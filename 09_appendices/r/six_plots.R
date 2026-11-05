#!/usr/bin/env Rscript
# Приложение B. Шесть корректных графиков на R.
# Запуск: Rscript 09_appendices/r/six_plots.R

suppressPackageStartupMessages({
  library(ggplot2)
  library(gridExtra)
  library(survival)
})

args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
script_path <- if (length(file_arg)) sub("^--file=", "", file_arg[1]) else "09_appendices/r/six_plots.R"
root <- normalizePath(file.path(dirname(script_path), "../.."), mustWork = TRUE)
df <- read.csv(file.path(root, "data/09_appendix_dataset.csv"), stringsAsFactors = FALSE)
df$group <- factor(df$group, levels = c("Контроль", "Препарат A", "Препарат B"))
pal <- c("Контроль" = "#7F7F7F", "Препарат A" = "#0072B2", "Препарат B" = "#D55E00")

theme_set(
  theme_bw(base_size = 8) +
    theme(
      panel.grid.minor = element_blank(),
      panel.grid.major.x = element_blank(),
      legend.position = "bottom",
      legend.title = element_blank(),
      legend.text = element_text(size = 5.5),
      legend.key.width = unit(0.35, "lines"),
      legend.key.height = unit(0.45, "lines"),
      legend.spacing.x = unit(0.12, "cm"),
      legend.margin = margin(0, 0, 0, 0),
      plot.title = element_text(size = 8.5, face = "bold"),
      axis.title = element_text(size = 7),
      axis.text = element_text(size = 6.5)
    )
)

agg <- aggregate(
  sbp_mm_hg ~ group + week, data = df,
  FUN = function(x) c(mean = mean(x), sd = sd(x), n = length(x))
)
agg <- do.call(data.frame, agg)
names(agg) <- c("group", "week", "mean", "sd", "n")
agg$ci <- 1.96 * agg$sd / sqrt(agg$n)

p1 <- ggplot(agg, aes(week, mean, color = group)) +
  geom_errorbar(aes(ymin = mean - ci, ymax = mean + ci), width = 0.35, linewidth = 0.5) +
  geom_line(linewidth = 0.7) +
  geom_point(size = 1.4) +
  scale_color_manual(values = pal) +
  scale_x_continuous(breaks = c(0, 4, 8, 12)) +
  labs(title = "A. САД по неделям", x = "Неделя", y = "САД, мм рт. ст.")

patients <- df[!duplicated(df$patient_id), ]
p2 <- ggplot(patients, aes(bmi_kg_m2, glucose_mmol_l, color = group)) +
  geom_point(alpha = 0.45, size = 1) +
  geom_smooth(method = "loess", se = FALSE, linewidth = 0.7) +
  scale_color_manual(values = pal) +
  labs(title = "B. BMI и глюкоза", x = "BMI, кг/м²", y = "Глюкоза, ммоль/л")

wide <- reshape(
  df[, c("patient_id", "group", "week", "sbp_mm_hg")],
  idvar = c("patient_id", "group"), timevar = "week", direction = "wide"
)
wide$change <- wide$sbp_mm_hg.12 - wide$sbp_mm_hg.0
p3 <- ggplot(wide, aes(group, change, fill = group)) +
  geom_boxplot(width = 0.55, outlier.shape = NA, alpha = 0.35, linewidth = 0.4) +
  geom_jitter(width = 0.12, size = 0.9, alpha = 0.6, color = "#333333") +
  geom_hline(yintercept = 0, linetype = "dashed", linewidth = 0.4, color = "#777777") +
  scale_fill_manual(values = pal) +
  labs(title = "C. Δ САД к 12-й неделе", x = NULL, y = "Δ САД, мм") +
  theme(legend.position = "none")

chg <- aggregate(change ~ group, data = wide, FUN = function(x) c(mean = mean(x), sd = sd(x), n = length(x)))
chg <- do.call(data.frame, chg)
names(chg) <- c("group", "mean", "sd", "n")
chg$ci <- qt(0.975, chg$n - 1) * chg$sd / sqrt(chg$n)
p4 <- ggplot(chg, aes(group, mean, fill = group)) +
  geom_col(width = 0.55) +
  geom_errorbar(aes(ymin = mean - ci, ymax = mean + ci), width = 0.15, linewidth = 0.5) +
  geom_hline(yintercept = 0, linewidth = 0.4, color = "#777777") +
  scale_fill_manual(values = pal) +
  labs(title = "D. Среднее Δ и 95 % ДИ", x = NULL, y = "Δ САД, мм") +
  theme(legend.position = "none")

p5 <- ggplot(agg, aes(factor(week), group, fill = mean)) +
  geom_tile(color = "white", linewidth = 0.6) +
  geom_text(aes(label = sprintf("%.0f", mean), color = mean), size = 2.2, show.legend = FALSE) +
  scale_fill_viridis_c(option = "C") +
  scale_color_gradient(low = "#333333", high = "#FFFFFF", guide = "none") +
  labs(title = "E. САД: группа × неделя", x = "Неделя", y = NULL, fill = "мм") +
  theme(legend.position = "right", legend.key.height = unit(0.6, "lines"))

fit <- survfit(Surv(time_months, event) ~ group, data = patients)
strata <- rep(names(fit$strata), fit$strata)
km <- data.frame(
  group = sub("^group=", "", strata),
  time = fit$time,
  surv = fit$surv
)
km$group <- factor(km$group, levels = levels(df$group))
cens <- data.frame(
  group = sub("^group=", "", strata)[fit$n.censor > 0],
  time = fit$time[fit$n.censor > 0],
  surv = fit$surv[fit$n.censor > 0]
)
cens$group <- factor(cens$group, levels = levels(df$group))
p6 <- ggplot(km, aes(time, surv, color = group)) +
  geom_step(linewidth = 0.8) +
  geom_point(data = cens, shape = 3, size = 1.2) +
  scale_color_manual(values = pal) +
  coord_cartesian(ylim = c(0, 1)) +
  labs(title = "F. Выживаемость (KM)", x = "Месяцы", y = "Выживаемость") +
  theme(legend.position = "bottom")

out <- file.path(root, "images/09_r_six.png")
png(out, width = 170, height = 110, units = "mm", res = 300)
grid.arrange(p1, p2, p3, p4, p5, p6, ncol = 3)
dev.off()
cat("saved:", out, "\n")
