import openai


openai.api_key = "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"
prompt_history = ""
while True:
    prompt_history = "Pyra: "+str(input("enter message: "))+"\nRex:"
    response = openai.Completion.create(
      model="davinci:ft-personal-2023-07-27-22-42-57",
      prompt=prompt_history,
      temperature=0.55,  # controls randomness
      max_tokens=200, # controls max length, do not increase, more tokens = more $$$$
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      stop=["Pyra: ", "Zeke:", "Mythra:", "Rex:"]
    )
    try:print("called " + str(response['choices'][0]['text']))
    except:print("No response/ error occured ")