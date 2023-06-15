import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY


class JobAssistant:
    """Generates data for a job offer using OpenAI's API.

    This class takes a job position and job offer, and generates a response
    including the key technical skills required for the job, three main responsibilities,
    and six interview questions.

    Attributes:
        job_posistion (str): The name of the job position.
        job_offer (str): The details of the job offer.
        gpt_response (dict): The response from the OpenAI API.
    """

    POMPT_ROLE = "You are an expert hiring manager with over 20 years of experience working with job seekers trying to land a role \
    in software development."
    PROMPT_TASK = "Based on this, draft the key technical skills/technical stack, highlight the three most important responsibilities, \
    and create six interview questions."

    def __init__(self, job_posistion, job_offer):
        """Initializes JobAssistant with job position and job offer.

        Args:
            job_posistion (str): The name of the job position.
            job_offer (str): The details of the job offer.
        """
        self.gpt_response = None
        self.job_posistion = job_posistion
        self.job_offer = job_offer

    def send_request(self):
        """Sends a request to the OpenAI API based on the job position and offer and constant class prompts.

            Raises:
            openai.error.APIError: If the OpenAI API returns an error.
                This could happen if the API request is not successful or there's an issue with the request.
            openai.error.APIConnectionError: If a connection to the OpenAI API cannot be established.
            openai.error.RateLimitError: If the request to the OpenAI API exceeds the rate limit.
            Exception: If an unexpected error occurs.

        Returns:
            str: An error message in case an exception is raised. If no exception is raised, returns '200'.
        """
        try:
            request_context = f"Consider the following job offer for {self.job_posistion}:\n{self.job_offer}"
            self.gpt_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                        "content": f"{self.POMPT_ROLE} {request_context} {self.PROMPT_TASK}",
                    }
                ],
            )
            return "200"
        except openai.error.APIError as e:
            # Handle API error here, e.g. retry or log
            return f"OpenAI API returned an API Error: {e}"
        except openai.error.APIConnectionError as e:
            # Handle connection error here
            return f"Failed to connect to OpenAI API: {e}"
        except openai.error.RateLimitError as e:
            # Handle rate limit error (we recommend using exponential backoff)
            return f"OpenAI API request exceeded rate limit: {e}"
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return f"An unexpected error occurred."

    def get_styled_answer(self):
        """Retrieves the generated response from the OpenAI API.

        Returns:
            str: The generated response from the OpenAI API.

        Raises:
            Exception: If send_request has not been called before this method.
        """
        if not self.gpt_response:
            raise Exception(
                "You need to call `send_request` before calling `get_styled_answer`."
            )

        answer = self.gpt_response["choices"][0]["message"]["content"]
        return answer


if __name__ == "__main__":
    # offer = "offer"
    # posistion = "Python backend engineer"

    # assistant = JobAssistant(posistion, offer)
    # assistant.send_request()
    # answer = assistant.get_styled_answer()
    # print(answer)
    pass
