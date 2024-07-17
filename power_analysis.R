# Fragen an Betreuer: passt unser d? 


#install.packages("pwr", lib = "D:/Programme/R-4.4.1/library")
require("pwr")
#install.packages('WebPower', lib = "D:/Programme/R-4.4.1/library")
require("WebPower")
#install.packages("effectsize", lib = "D:/Programme/R-4.4.1/library")
library("effectsize")
# Searches for absent human faces were faster when distractors were otters compared to chimpanzees, with an effect size d=0.6


# Cohens d to cohens f function

# cohens_d_to_cohens_f = function(d){
# cohens_f = d/2                          # Formel korrekt -> ist Anzahl der Gruppen (k) = 2
#  return(cohens_f)
# }

cohens_d_to_cohens_f = function(d){
  cohens_f = d/sqrt(2)                          # Formel korrekt -> ist Anzahl der Gruppen (k) = 1 (weil ng = 1)
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
n_epochs = 6                # Produkt aller Faktorstufen (3x2)
dis_configuration = 3       # Anzahl der Level/ Faktorstufen (Display size?)                    
ng = 1



(cohens_f = cohens_d_to_cohens_f(d))    # Klammern entsprechen print

# in cohens F transformieren

df1 = (dis_configuration - 1)*(n_epochs - 1)
df_err = (dis_configuration - 1)*(n_epochs - 1)*(n - 1)

(power_rmANOVA = wp.rmanova(ng = 1, nm = n_epochs, f = cohens_f, nscor = 1, alpha = 0.05, power = power, type = 1))   # wir suchen Interaktionseffekt


# Repeated-measures ANOVA analysis

#           n        f ng nm nscor alpha power
#   11.16068 1.131371  1  6     1  0.05   0.8

# NOTE: Power analysis for within-effect test
