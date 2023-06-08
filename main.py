from flask import Flask, render_template, request
import openai
import time

app = Flask(__name__)
messages = []

# Set up OpenAI API credentials
openai.api_key = "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"

# Define a function to query OpenAI GPT-3 API and get answer
def generate_answer(question):
    # Define prompt
    prompt = f"Answer the following question: {question}\nAnswer:"

    # Generate response from OpenAI GPT-3 API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extract answer from response
    answer = response.choices[0].text.strip()

    # Return answer
    return answer

@app.route("/")
def animation():
    return render_template("animation.html")

@app.route("/index.html")
def index():
    # Wait for 3 seconds before rendering the index.html template
    time.sleep(3)
    return render_template("index.html")

@app.route("/get_answer", methods=["POST"])
def get_answer():
    # Get question from form
    question = request.form["question"]
    
    # Append user message to messages list
    messages.append({"text": question, "sender": "user"})
    
    # Generate answer
    answer = generate_answer(question)
    
    # Append chatbot response to messages list
    messages.append({"text": answer, "sender": "bot"})
    
    # Render template with messages
    return render_template("index.html", messages=messages)

if __name__ == "__main__":
    app.run(debug=True)
