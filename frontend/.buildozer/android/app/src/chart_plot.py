from kivy.uix.image import Image
import matplotlib.pyplot as plt
import tempfile

class Charts:
    def create_piechart(self, data_dict: dict):
        colors = ['red', 'yellow', 'orange', 'green', 'pink', 'blue', 'aquamarine']
        fig, ax = plt.subplots()
        ax.pie(list(data_dict.values()), labels=list(data_dict.keys()), colors=colors, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmpfile:
            fig.savefig(tmpfile.name)
            image_path = tmpfile.name
        chart = Image(source=image_path)
        return chart
    
    def create_barschart(self, data_dict: dict):
        colors = ['red', 'yellow', 'orange', 'green']
        fig, ax = plt.subplots()
        bars = ax.bar(list(data_dict.keys()), list(data_dict.values()), color=colors)
        ax.set_xticklabels([])
        ax.legend(bars, data_dict.keys())  # Add legend with bar labels
        
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmpfile:
            fig.savefig(tmpfile.name)
            image_path = tmpfile.name
        chart = Image(source=image_path, size_hint=(1, 0.8))
        return chart