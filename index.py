import tkinter as tk
import openai

openai.api_key = "API_KEY"

root = tk.Tk()
root.title("ChatGPT")
root.geometry("600x600")
input_box = tk.Entry(root, font=("Arial", 14), width=40)
input_box.pack(pady=20)
output_box = tk.Text(root, font=("Arial", 12), width=70, height=20)
output_box.pack(pady=20)

def send_message():
    message = input_box.get()
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "user", "content": message}],
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=1,
    )

    reply = ''
    for choice in response.choices:
      reply += choice.message.content

    output_box.insert(tk.END, "AI: " + reply + "\n\n")
    output_box.see(tk.END)
    input_box.delete(0, tk.END)

send_button = tk.Button(root, text="Gönder", font=("Arial", 14), command=send_message)
send_button.pack()
root.mainloop()
