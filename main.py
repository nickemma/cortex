import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import ClientError, ServerError


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

    print("Response")
    print(response.text)


if __name__ == "__main__":
    main()
