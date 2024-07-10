# Fragen an Betreuer: passt unser d & Typ 1 oder Typ 2 ANOVA


#install.packages("pwr", lib = "D:/Programme/R-4.4.1/library")
require("pwr")
#install.packages('WebPower', lib = "D:/Programme/R-4.4.1/library")
require("WebPower")
#install.packages("effectsize", lib = "D:/Programme/R-4.4.1/library")
library("effectsize")
# Searches for absent human faces were faster when distractors were otters compared to chimpanzees, with an effect size d=0.6


# Cohens d to cohens f function

cohens_d_to_cohens_f = function(d){
  cohens_f = d/2                          # Formel korrekt -> ist Anzahl der Gruppen (k) = 2
  return(cohens_f)
}


# T-Test-Variante
power = 0.8                    # power level
alpha = 0.05                   # alpha level
d = mean(c(1.81, 1.39))              # effect size -> human face compared to nonhuman animal face, human face absent für alle Distraktoren
# 0.97 (nur im Zweifel, human faces für kontrollierte Distraktoren)
(power_paired_t = pwr.t.test(d = d, sig.level = alpha, 
                             power = power, type = c("paired"),
                             alternative = "two.sided"))


# repeated measure ANOVA -> >2 MW
n = 33                      # n aus Beispielpaper
n_epochs = 2                # Anzahl der measurements (anwesen/abwesend?)
dis_configuration = 3       # Anzahl der Level  (Display size?)


(cohens_f = cohens_d_to_cohens_f(d))    # Klammern entsprechen print

# in cohens F transformieren

df1 = (dis_configuration - 1)*(n_epochs - 1)
df_err = (dis_configuration - 1)*(n_epochs - 1)*(n - 1)

# (f_cohen = F_to_f(F_val, df1, df_err, ci = 0.95, alternative = "less", squared = F))


(power_rmANOVA = wp.rmanova(ng = dis_configuration, nm = n_epochs, f = cohens_f, nscor = 1, alpha = 0.05, power = power, type = 2))   # wir suchen Interaktionseffekt


