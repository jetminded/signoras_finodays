from catboost import CatBoostRegressor
import pandas as pd


def apartments_predict(walls_material, floor_number, floors_total, total_area, kitchen_area, distance, azimuth):
    model = CatBoostRegressor()
    model.load_model('apartments_model')
    data = {
        'wallsMaterial': [walls_material],
        'floorNumber': [floor_number],
        'floorsTotal': [floors_total],
        'totalArea': [total_area],
        'kitchenArea': [kitchen_area],
        'distance': [distance],
        'azimuth': [azimuth]
    }
    df = pd.DataFrame(data)
    print(model.predict(df)[0])


apartments_predict('panel', 16, 17.0, 55.0, 9.2, 17568.0, 304.0)

