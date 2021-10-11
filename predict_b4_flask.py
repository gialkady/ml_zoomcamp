import pickle


model_file = 'model1.bin'
Dict_Vectorizer ='dv.bin'


with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

with open(Dict_Vectorizer, 'rb') as f_in:
    dv = pickle.load(f_in)

customer = {"contract": "two_year", "tenure": 12, "monthlycharges": 19.7}

def predict (customer):

    X = dv.transform([customer]) #turn the customer in to feature matrix to be used by dv
    y_pred= model.predict_proba(X)[0,1]
    churn = y_pred >=0.5

    result = {'churn_probability': round(float(y_pred),3),
              'churn': bool(churn)
              }

    return result


pred_customer= predict(customer)

if pred_customer ['churn'] == True:
    print('sending promo email to %s' %('xyz-123'))





