# %matplotlib inline  # magic
import pandas as pd
import matplotlib.pyplot as plt
import sys
import click

# dir stuff
# import os
# os.getcwd()
# os.chdir(r'C:\Users\lknogler\Desktop\python\nick\Day1')
   
# filename = 'oktoberfestgesamt19852016.csv' 

@click.group()
def cli():
    """Can display and plot csv files"""
    pass

@cli.command()
@click.argument('filename')
def display(filename):
    """Displays column names and data type"""
    df=pd.read_csv(filename)
    # df.head()  # first 5 rows
    print(df.dtypes)

@cli.command()
@click.argument('filename')
@click.option('--column', default=None, help='Name of column to plot, inputted as --column column_name')
def plot(filename, column):
    """Plots a histogram of one or all column(s) of the csv file"""
    df=pd.read_csv(filename)
    if column is None:
        df.hist();
    else:
        df[column].hist()
    plt.show()  # if slow, this blocks all subsequent code from running # it waits for the window to close before continuing

# called in terminal as: python csv_parser.py command filename --column column_name    
    
if __name__ == '__main__':
    # display_columns()
    # plot_hist()
    cli()