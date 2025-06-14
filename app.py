def main(selected_item, input_message):
    from dotenv import load_dotenv
    load_dotenv()
    from langchain_openai import ChatOpenAI
    from langchain.schema import SystemMessage, HumanMessage

    if selected_item == "株主投資":
        llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
        messages = [
            SystemMessage(content=("あなたは株式投資の専門家です。ユーザーの質問に対して専門的な知識をもとに回答してください。株主投資に関連しない質問には丁寧に断って回答しないでください。")),
            HumanMessage(content=input_message),
        ]
    else:
        llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
        messages = [
            SystemMessage(content=("あなたは日本の歴史の専門家です。ユーザーの質問に対して専門的な知識をもとに回答してください。歴史に関連しない質問には丁寧に断って回答しないでください。")),
            HumanMessage(content=input_message),
        ]

    result = llm(messages)
    return result.content  # 結果を返すように変更

import streamlit as st
st.title("専門家への質問アプリ")
st.write("#### 各モードに関係がない質問にはお答えできません。")
st.write("##### 動作モード1: 株式投資に関する質問")
st.write("入力フォームに株式投資に関する質問を入力し、「実行」ボタンを押すことで質問の回答が得られます。")
st.write("##### 動作モード2: 日本の歴史に関する質問")
st.write("入力フォームに日本の歴史に関する質問を入力し、「実行」ボタンを押すことで質問の回答が得られます。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["株主投資", "日本の歴史"]
)

st.divider()

if selected_item == "株式投資":
    input_message = st.text_input(label="株式投資に関する質問を入力してください")

else:
    input_message = st.text_input(label="日本歴史に関する質問を入力してください")

if st.button("実行"):
    st.divider()
    st.write("##### 結果")
    if input_message.strip():  # 入力が空でない場合のみ実行
        result = main(selected_item, input_message)
        st.write(result)  # LLMの結果を画面に表示
    else:
        st.write("質問を入力してください。")