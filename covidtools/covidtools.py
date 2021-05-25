import pandas as pd
import numpy as np
import plotly.express as px


class LiliHomework:

    def __init__(self, result):
      self.result = result

    def __repr__(self):
        return f"data on Covid: {self.result}"
    
    def __len__(self):
      return len(self.result)
  
    def plot(self):
      return px.line(self.result)
    
    def sum(self):
        return sum(self.result)

    def save(self):
        filename = 'CovidData.xlsx'
        result = self.result
        df = pd.DataFrame([self.result],)
        df.to_excel('CovidData.xlsx')
        print('Data is written to Excel File successfully.')
