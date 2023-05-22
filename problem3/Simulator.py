import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from sklearn import metrics
class GeneSimulator():
    def __init__(self,health_cases=10,patient_cases=10, gene_count=12500,different_count=1250,alpha=0.01):
        self.health_cases = health_cases
        self.patient_cases = patient_cases
        self.gene_count = gene_count
        self.different_count = different_count
        self.alpha = alpha
        self.GenerateSimulatedData(health_cases,patient_cases,gene_count,different_count)

    def GenerateSimulatedData(self,health_cases,patient_cases, gene_count, different_count):
        np.random.seed(42)
        # loc is mean and scale is standard deviation
        self.healthy_datas = np.random.normal(loc=10, scale=2, size=(health_cases, gene_count))
        self.cancer_datas = np.random.normal(loc=10, scale=2, size=(patient_cases, gene_count))
        self.data = np.concatenate((self.healthy_datas, self.cancer_datas))
        self.data[:10,0:different_count]+=2
        self.data[10:,0:different_count]-=2
    def CalcT_Test(self):
        p_values = []
        t_tests = []
        for col_index in range(self.data.shape[1]):
            health_group = self.data[0:self.health_cases,col_index]
            patient_group = self.data[self.health_cases:,col_index]
            tval, pval = stats.ttest_ind(health_group, patient_group)
            #print(col_index,pval)
            t_tests.append(tval)
            p_values.append(pval)
        return t_tests,p_values
    def CalcWilcoxon_Test(self):
        p_values = []
        t_tests = []
        for col_index in range(self.data.shape[1]):
            health_group = self.data[0:self.health_cases,col_index]
            patient_group = self.data[self.health_cases:,col_index]
            tval, pval = stats.wilcoxon(health_group, patient_group)
            #print(col_index,pval)
            t_tests.append(tval)
            p_values.append(pval)
        return t_tests,p_values
    def CalcKruskal_Test(self):
        p_values = []
        t_tests = []
        for col_index in range(self.data.shape[1]):
            health_group = self.data[0:self.health_cases,col_index]
            patient_group = self.data[self.health_cases:,col_index]
            tval, pval = stats.kruskal(health_group, patient_group)
            #print(col_index,pval)
            t_tests.append(tval)
            p_values.append(pval)
        return t_tests,p_values
    def BarPlot(self,p_values,plot_name):
        plt.figure(figsize=(10,3),dpi=300)
        x= range(0,len(p_values))
        colors = []
        for item in p_values:
            if item<0.01:
                colors.append('green')
            else:
                colors.append('red')
        plt.bar(x,p_values,color = colors)
        plt.yscale('log')
        plt.ylabel("P-Value (log scale)")
        plt.title(plot_name)

        plt.savefig(f"{plot_name}.png")
    def PowerPlot(self,p_values,plot_name):
        plt.figure(figsize=(10,3),dpi=300)
        x= range(0,len(p_values))
        plt.plot(x,np.array(p_values)**2)
        plt.yscale('log')
        plt.ylabel("P-Value (log scale)")
        plt.title(plot_name)

        plt.savefig(f"{plot_name}.png")
    def CalcConfusionMatrix(self,p_values):
        import math
        confusion = np.zeros((2,2))
        for index,p_value in enumerate(p_values):
            if index < self.different_count:
                if p_value<= self.alpha:
                    confusion[1,1]+=1
                else:
                    confusion[0,1]+=1
            else:
                if p_value >= self.alpha:
                    confusion[0,0]+=1
                else:
                    confusion[1,0]+=1
        confusion = confusion / confusion.sum(axis=1)
        return confusion
    def CalcConfusionMatrixUsingFunction(self,p_values):
        import math
        actual_label = np.zeros(len(p_values))
        predicted_label = np.zeros(len(p_values))
        for index,p_value in enumerate(p_values):
            if index < self.different_count:
                actual_label[index] = 1
                if p_value<= self.alpha:
                    predicted_label[index] = 1
                else:
                    predicted_label[index] = 0
            else:
                actual_label[index] = 0
                if p_value >= self.alpha:
                    predicted_label[index]=0
                else:
                    predicted_label[index] = 1

        confusion = metrics.confusion_matrix(actual_label, predicted_label,normalize='true')
        return confusion
    def PlotConfusionMatrix(self,confusion_matrix,name):
        plt.figure(figsize=(5, 5), dpi=70)
        cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix, display_labels=[False, True])
        cm_display.plot()
        plt.savefig(f"{name}.png")
    def PrintData(self):
        print(self.healthy_datas)
        print(self.cancer_datas)
