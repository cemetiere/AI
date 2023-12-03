from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

def lsm(X_train, y_train):
    # Добавим столбец с единицами для учёта свободного члена
    X = np.column_stack((np.ones(X_train.shape[0]), X_train))

    # Вычислим коэффициентов линейной регрессии методом наименьших квадратов
    coefficients = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y_train)

    return coefficients

# Получим предсказания для тестового набора данных
def predict(X_test, coefficients):
    # Добавим столбец с единицами для учёта свободного члена
    X = np.column_stack((np.ones(X_test.shape[0]), X_test))

    # Предскажем значения
    y_pred = X.dot(coefficients)
    return y_pred


def determination_coeff(y_test, y_pred):
    total_variance = np.sum((y_test - np.mean(y_test)) ** 2)
    residual_variance = np.sum((y_test - y_pred) ** 2)
    dc = 1 - (residual_variance / total_variance)
    return dc



data = pd.read_csv('Student_Performance.csv')
data['Extracurricular Activities'].replace({
    'Yes': 1,
    'No': 0
}, inplace=True)

X = data.drop(columns=['Performance Index'])  # Признаки, исключая 'Performance Index'
y = data['Performance Index']  # Целевая переменная 'Performance Index'


# Модель 1 по всем признакам
columns = ['Hours Studied', 'Previous Scores', 'Extracurricular Activities', 'Sleep Hours', 'Sample Question Papers Practiced']
X_train_1, X_test_1, y_train, y_test = train_test_split(data[columns], y, test_size=0.8, random_state=336630)
coefficients1 = lsm(X_train_1.values, y_train.values)
y_pred_1 = predict(X_test_1.values, coefficients1)
print('Предсказания модели 1:', y_pred_1)
print('Коэффициент детерминации:', determination_coeff(y_test, y_pred_1),'\n')


# Модель 2 по признаку Sleep Hours и Previous Scores
columns = ['Sleep Hours', 'Previous Scores']
X_train_2, X_test_2, y_train, y_test = train_test_split(data[columns], y, test_size=0.6, random_state=336630)
coefficients2 = lsm(X_train_2.values, y_train.values)
y_pred_2 = predict(X_test_2.values, coefficients2)
print('Предсказания модели 2:', y_pred_2)
print('Коэффициент детерминации:', determination_coeff(y_test, y_pred_2),'\n')


# Модель 3 по признаку Previous Scores
columns = ['Previous Scores']
X_train_3, X_test_3, y_train, y_test = train_test_split(data[columns], y, test_size=0.3, random_state=336630)
coefficients3 = lsm(X_train_3.values, y_train.values)
y_pred_3 = predict(X_test_3.values, coefficients3)
print('Предсказания модели 3:', y_pred_3)
print('Коэффициент детерминации:', determination_coeff(y_test, y_pred_3))
