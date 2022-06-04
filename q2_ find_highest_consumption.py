# Import your libraries
import pandas as pd

# make smaller variables for ease while testing code
eu = fb_eu_energy
asia= fb_asia_energy
na= fb_na_energy


#concatenate dataframes into 1
df = pd.concat([eu,asia,na])
#groupby date, aggregate consumption by date and sort values in descenting order
cbd = df. groupby('date', as_index = False)['consumption'].sum().sort_values(by = ['consumption'], ascending = False)
# slice dataframe by values that match the maximum consumption value
answer = cbd[cbd['consumption']==cbd['consumption'].max()]
#call answer variable 
answer


#answer as a function to input into a executable script

# Call to inport dataframe from source
#write call here

def find_highest_consumption(x,y,z):
	df = pd.concat([x,y,z])
	cbd = df. groupby('date', as_index = False)['consumption'].sum().sort_values(by = ['consumption'], ascending = False)
	answer = cbd[cbd['consumption']==cbd['consumption'].max()]
	return answer

def main():
	find_highest_consumption(eu,asia,na)
	
if __name__ == "__main__":
    main()