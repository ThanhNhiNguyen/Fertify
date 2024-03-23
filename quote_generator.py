import openai

# Set up your OpenAI API key
openai.api_key = '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'

# Prompt for generating the quote
prompt = "Generate a quote of the day about protecting the environment."

# Generate the completion
response = openai.Completion.create(
  engine="davinci", 
  prompt=prompt, 
  temperature=0.7,
  max_tokens=50
)

# Extract and print the generated quote
quote = response.choices[0].text.strip()
print("Environment Quote: ")
print(quote)