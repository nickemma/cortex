import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import ClientError, ServerError

from call_function import available_functions
from prompts import system_prompt


def main():
    print("Hello from cortex!")

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError(
            "GEMINI_API_KEY not found. Make sure it is set in your .env file."
        )

    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="cortex")
    parser.add_argument("user_prompt", type=str)
    parser.add_argument("--verbose", action="store_true")

    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                tools=[available_functions],
                temperature=0,
            ),
        )

    except (ServerError, ClientError):
        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print("Prompt tokens: 0")
            print("Response tokens: 0")

        print("Response")
        print("Error: Gemini API temporarily unavailable or quota exceeded.")
        return

    if response.usage_metadata is None:
        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print("Prompt tokens: 0")
            print("Response tokens: 0")

        print("Response")
        print("Error: missing usage metadata")

    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

    if response.function_calls:
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(response.text)


if __name__ == "__main__":
    main()
