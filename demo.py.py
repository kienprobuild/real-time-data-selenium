from flask import Flask, render_template, url_for, request
import pandas as pd
import numpy as np
#data =pd.read_csv("./twitter.csv")
# data["user_sentiment"]=data["user_sentiment"].map({"positive":0,"neutral":2,"negative":1})
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(
#  data["text"], data["user_sentiment"], test_size=0.2, random_state=42)
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# tokenizer=Tokenizer(num_words=10000,oov_token="<OOV>")
# tokenizer.fit_on_texts(X_train)
# import tensorflow as tf
# new_model = tf.keras.models.load_model('./kien.h5')
# test=tokenizer.texts_to_sequences([" ngo le hieu kien"])
# padd_test=pad_sequences(test,maxlen=140,truncating='post',padding='post')
# name=new_model.predict(padd_test)
#print(name)
import pandas as pd
data =pd.read_csv("./tweet_data_preprocessing.csv",encoding= 'unicode_escape')
data["sentence"]=data["sentence"].astype(str)
data["label"]=data["label"].map({"positive":0,"neutral":2,"negative":1})
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
 data["sentence"], data["label"], test_size=0.2, random_state=42)
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
tokenizer=Tokenizer(num_words=10000,oov_token="<OOV>")
tokenizer.fit_on_texts(X_train)
import tensorflow as tf
new_model = tf.keras.models.load_model('./demo.h5')
app = Flask(__name__)

 

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")



@app.route('/result',methods=['POST', 'GET'])
def result():
    user_input = request.form['name']
    url = user_input
    # test=tokenizer.texts_to_sequences(data)
    # padd_test=pad_sequences(test,maxlen=140,truncating='post',padding='post')
    # a=new_model.predict(padd_test)
    # b=max(a)
    from selenium import webdriver
    from time import sleep
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options


    options = Options()

    options.add_experimental_option('excludeSwitches', ['enable-logging'])

# 1. Khai báo browser
    browser = webdriver.Chrome(executable_path="./chromedriver",chrome_options=options)
# url = "https://shopee.sg/-Pre-Order-MSI-Optix-MAG274QRF-QD-Gaming-Monitor-(27inch-WQHD-Rapid-IPS-Panel-165hz-1ms-G-Sync-3Y)-i.235042613.6761847522?sp_atk=4a4f3668-b0be-45ff-b89a-e861279f7c14"
    #url = "https://shopee.sg/Einashop-2-Piece-Bundle-Clio-Casual-Shorts-i.16613456.7041213170?sp_atk=02d0521b-f36e-4f4c-acea-98c9110d2d0e"
# 2. Mở URL của post
    browser.get(url)
    sleep(3)

    browser.execute_script("window.scrollTo(0," + "300" + " )") 

    sleep(5)
    element = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div/div[3]/div[2]/div[1]/div[1]");
#get x, y coordinates//*[@id='main']/div/div[2]/div[1]/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[1]/div[2]/div[2]/div

    loc = element.location
#get height, width
    s = element.size

    h = str(loc["y"] + s["height"])
    browser.execute_script("window.scrollTo(0," + h + " )") 
    sleep(5)


# sleep(5)

# # 3. Lấy link hiện comment
# #browser.find_elements_by_class_name("shopee-product-rating__main")
    a=browser.find_elements_by_class_name("shopee-product-rating__main")
# print(a)
# # # 3. Lấy link hiện comm
# # comment_list = browser.find_element_by_class_name("_3NrdYc")
    l=[]
    for i in a:
        b=i.find_element_by_class_name("_3NrdYc")
        l.append(b.text)

    sleep(2)
    demo=tokenizer.texts_to_sequences(l)
    demo_pad=pad_sequences(demo,maxlen=140,truncating='post',padding='post')
    a=new_model.predict(demo_pad)
    s=[]
    for i in range(len(l)):
        s.append(np.argmax(a[i]))
    for i in range(len(s)):
        if s[i]==0:
            s[i]="positive"
        if s[i]==1:
            s[i]="negative"
        if s[i]==2:
            s[i]="neutral"
    out_tox = s[0]
    out_sev = s[1]
    out_obs = s[2]
    out_ins = s[3]
    out_thr = s[4]
    out_ide = s[5]
    


    browser.close()
    return render_template('index.html', 
                            pred_tox = l[0]+":" +'{}'.format(out_tox),
                            pred_sev = l[1]+":" + '{}'.format(out_sev), 
                            pred_obs = l[2]+ ":"+'{}'.format(out_obs),
                            pred_ins = l[3]+":" + '{}'.format(out_ins),
                            pred_thr = l[4]+ ":"+'{}'.format(out_thr),
                            pred_ide = l[5]+ ":" +'{}'.format(out_ide)                        
                            )



    return render_template('index.html', pred_tox = b)
    




if __name__ == "__main__":
    app.run(debug=True)