from random import randint

from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

class IndexView(TemplateView):
    template_name = 'index.html'

class DadosJSONView(BaseLineChartView):
    
    def get_labels(self):
        # Este método retorna 12 labels para eixo X
        labels = [
            "label1",
            "label2",
            "label3",
            "label4",
            "label5",
            "label6",
            "label7",
            "label8",
            "label9",
            "label0",
            "label11",
            "label12"
        ]
        return labels

    def get_providers(self):
        # Este método retorna o nome dos datasets
        datasets = [
            "Teste dataset1",
            "Teste dataset2",
            "Teste dataset3",
            "Teste dataset4",
            "Teste dataset5",
            "Teste dataset6",
        ]
        return datasets

    def get_data(self):
        # Este método retorna 6 datasets para plotar o gráfico
        # Cada linha representa um dataset
        # Cada coluna representa um label
        
        dados = []
        for l in range(6):
            for c in range(12):
                dado = [
                    randint(1, 200), #label1
                    randint(1, 200), #label2
                    randint(1, 200), #label3
                    randint(1, 200), #label4
                    randint(1, 200), #label5
                    randint(1, 200), #label6
                    randint(1, 200), #label7
                    randint(1, 200), #label8
                    randint(1, 200), #label9
                    randint(1, 200), #label10
                    randint(1, 200), #label11
                    randint(1, 200), #label12
                ]
            dados.append(dado)

        return dados