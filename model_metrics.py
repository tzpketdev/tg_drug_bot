import numpy as np
from aiogram import types, Router, F
import pandas as pd
import pickle
from aiogram.filters.command import CommandObject
from aiogram.filters import Command


def load_model() -> object:
    with open("drug-model.pk1", "rb") as f:
        model = pickle.load(f)
    return model


def load_encoders() -> object:
    with open("encoder_BP.pk1", "rb") as f:
        encoder_BP = pickle.load(f)

    with open("encoder_Cholesterol.pk1", "rb") as f:
        encoder_Cholesterol = pickle.load(f)

    with open("encoder_sex.pk1", "rb") as f:
        encoder_sex = pickle.load(f)

    with open("encoder_Drug.pk1", "rb") as f:
        encoder_Drug = pickle.load(f)

    dict_encoders = {
        "BP": encoder_BP,
        "Cholesterol": encoder_Cholesterol,
        "Sex": encoder_sex,
        "Drug": encoder_Drug,
    }
    return dict_encoders


router = Router()


@router.message(Command("predict"))
async def predict_one(message: types.Message, command: CommandObject):
    try:
        Age, Sex, BP, Cholesterol, Na_to_K = command.args.split(" ")
        dict_encoders = load_encoders()
        await message.answer(
            "Ваш ввод:\n"
            f"Age: {Age}, Sex: {Sex}, BP: {BP}\n"
            f"Cholesterol: {Cholesterol}, Na_to_K: {Na_to_K}"
        )
        BP_tr = dict_encoders["BP"].transform([BP])[0]
        Sex_tr = dict_encoders["Sex"].transform([Sex])[0]

        Cl_tr = dict_encoders["Cholesterol"].transform([BP])[0]
        features = np.array([[Age, Sex_tr, BP_tr, Cl_tr, Na_to_K]]).astype(float)

        model = load_model()
        features = pd.DataFrame(
            features, columns=["Age", "Sex", "BP", "Cholesterol", "Na_to_K"]
        )
        prediction = model.predict(features)
        predict_encode = dict_encoders["Drug"].inverse_transform(prediction)
        await message.answer(f"Предсказание модели: {predict_encode[0]}")
    except:
        answer = (
            "Введите данные следующим образом:\n"
            "Возраст Пол Кровяное_давление Уровень_холестерина "
            "Соотношение_натрия_к_калию\n"
            "Все данные пишите через пробел"
        )
        await message.answer(answer)
