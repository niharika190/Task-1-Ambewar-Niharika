{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e02bcd90-d5bc-46ae-bb79-71d5fd26479c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  HI\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Chatbot: Hello there, how can i help you?\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  gOOD morning\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Chatbot: A very good morning\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  who are you?\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Chatbot: I am a rule based chatbot\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  chatbot\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Chatbot: Sorry, I don't understand that.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  exit\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Chatbot: Session ended\n"
     ]
    }
   ],
   "source": [
    "responses={\n",
    "    \"hi\":\"Hello there, how can i help you?\",\n",
    "    \"hello\":\"Hi user.\",\n",
    "    \"good morning\":\"A very good morning\",\n",
    "    \"help me\":\"What do you want me to do.\",\n",
    "    \"who are you?\":\"I am a rule based chatbot\"}\n",
    "while True:\n",
    "    raw_input=input(\"You: \")\n",
    "    sanitized_input=raw_input.strip().lower()\n",
    "    if sanitized_input in [\"exit\",\"quit\"]:\n",
    "        print(\"Chatbot: Session ended\")\n",
    "        break\n",
    "    response=responses.get(sanitized_input,\"Sorry, I don't understand that.\")\n",
    "    print(\"Chatbot:\",response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "523ecf32-95c2-4d09-bb06-0fbe1fd60125",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
