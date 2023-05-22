from Simulator import GeneSimulator
if __name__ == "__main__":
    geneSimulator = GeneSimulator()

    _,pvalues = geneSimulator.CalcT_Test()
    geneSimulator.BarPlot(pvalues,"ttest")
    geneSimulator.PowerPlot(pvalues,"ttest_power")
    confustionMatrix = geneSimulator.CalcConfusionMatrixUsingFunction(pvalues)
    geneSimulator.PlotConfusionMatrix(confustionMatrix,"confusion_ttest")

    _,pvalues = geneSimulator.CalcWilcoxon_Test()
    geneSimulator.BarPlot(pvalues,"wilcoxon")
    geneSimulator.PowerPlot(pvalues,"wilcoxon_power")
    confustionMatrix = geneSimulator.CalcConfusionMatrixUsingFunction(pvalues)
    geneSimulator.PlotConfusionMatrix(confustionMatrix,"confusion_wilcoxon")

    _,pvalues = geneSimulator.CalcKruskal_Test()
    geneSimulator.BarPlot(pvalues,"kruskal_bar")
    geneSimulator.PowerPlot(pvalues,"kruslal_power")
    confustionMatrix = geneSimulator.CalcConfusionMatrixUsingFunction(pvalues)
    geneSimulator.PlotConfusionMatrix(confustionMatrix,"confusion_kruskal")