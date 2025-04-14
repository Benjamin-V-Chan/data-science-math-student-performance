import os
import matplotlib.pyplot as plt
import joblib
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def load_model_and_data(filepath):
    return joblib.load(filepath)

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return y_pred, mse, mae, r2

def plot_actual_vs_predicted(y_test, y_pred, output_path):
    plt.figure()
    plt.scatter(y_test, y_pred)
    plt.xlabel('Actual G3')
    plt.ylabel('Predicted G3')
    plt.title('Actual vs Predicted G3')
    plt.savefig(output_path)
    plt.close()
    
def main():
    model_file = os.path.join('..', 'outputs', 'model.pkl')
    eval_output = os.path.join('..', 'outputs', 'evaluation.txt')
    plot_output = os.path.join('..', 'outputs', 'actual_vs_predicted.png')
    model, X_test, y_test = load_model_and_data(model_file)
    y_pred, mse, mae, r2 = evaluate_model(model, X_test, y_test)
    with open(eval_output, 'w') as f:
        f.write(f'MSE: {mse}\nMAE: {mae}\nR2 Score: {r2}\n')
    plot_actual_vs_predicted(y_test, y_pred, plot_output)

if __name__ == '__main__':
    main()
