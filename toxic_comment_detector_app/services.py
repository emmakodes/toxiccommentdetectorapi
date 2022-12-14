import pickle
from rest_framework import status
from rest_framework.response import Response


def check_toxicity(comment):
    comment_dictionary = {}
    comment_dictionary['comment_key'] = [comment]

    # load the vectorizer and vectorize comment
    vectorizer = pickle.load(open("./Vectorize.pickle", "rb"))
    testing = vectorizer.transform(comment_dictionary['comment_key'])

    # load the model
    with open('./Pickle_LR_Model.pkl', 'rb') as file:
        lr_model = pickle.load(file)

    # predict toxicity. prediction range from 0.0 to 1.0 (0.0 = non-toxic and 1.0 toxic)
    prediction = lr_model.predict_proba(testing)[:, 1]
    prediction = float(prediction)

    if prediction >= 0.9 and prediction <= 1.0:
        response_list = ["toxic comment", prediction]
        return Response({"response": response_list}, status=status.HTTP_200_OK)

    elif prediction >= 0.0 and prediction <= 0.1:
        response_list = ["non toxic comment", prediction]
        return Response({"response": response_list}, status=status.HTTP_200_OK)

    else:
        response_list = ["Manually check this", prediction]
        return Response({"response": response_list}, status=status.HTTP_200_OK)
