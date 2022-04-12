import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler



class mlengine:
    def __init__(self, file):
        self.file = file
        self.dataframe = pd.read_csv(file,sep=",")
        self.df_linear = self.dataframe.loc[:, ['SqFt', 'Sold']]
        self.accuracy = 0
    def df(self):
        return self.df_linear

    def dataframe(self):
        return self.dataframe

    def accuracy(self):
        return str(self.accuracy)

    def dfarray(self):
        nparray = self.df_linear.to_numpy()
        result = []
        for item in enumerate(nparray):
            result.append([item[1][0], item[1][1]])
        return result

    def multivariate(self):
        # categorize the condo complexes from strings
        df_multivariate = pd.get_dummies(self.dataframe, columns=['Complex'], prefix='', prefix_sep='')

        # list of columns to scale
        cols_to_scale = ['Beds', 'Bath', 'SqFt']

        # scale all the independent features
        scaler = StandardScaler()
        scaler.fit(df_multivariate[cols_to_scale])
        df_multivariate[cols_to_scale] = scaler.transform(df_multivariate[cols_to_scale])

        # drop columns we don't need (include a condo category to avoid dummy variable trap
        df_multivariate = df_multivariate.drop(['List', 'SoldDate', 'Hudson'], axis=1)

        features = df_multivariate.drop(['Sold'], axis=1)
        target = df_multivariate['Sold']

        regressor = LinearRegression()

        # fit our features and target to our linear regression
        regressor.fit(features, target)

        self.accuracy = round(regressor.score(features, target)*100, 2)
        #print('Accuracy:', regressor.score(features,target))


