import csv
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  system_instruction="""
  Devolver en este formato 
      Solución en python del problema: ´´´ ´´´ 
      Input 1 del problema: ´´´ ´´´
      Output 1 del problema: ´´´ ´´´
      Input 2 del problema: ´´´ ´´´
      Output 2 del problema: ´´´ ´´´
      Input 3 del problema: ´´´ ´´´
      Output 3 del problema: ´´´ ´´´
  """,
)

chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message("""
1,Two Sum,"Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
`2 <= nums.length <= 103`
`-109 <= nums[i] <= 109`
`-109 <= target <= 109`
Only one valid answer exists.",0,Easy,/articles/two-sum,46.7,100.0,https://leetcode.com/problems/two-sum,999,4.1M,8.7M,"Amazon,Google,Apple,Adobe,Microsoft,Bloomberg,Facebook,Oracle,Uber,Expedia,Twitter,Nagarro,SAP,Yahoo,Cisco,Qualcomm,tcs,Goldman Sachs,Yandex,ServiceNow","Array,Hash Table",20217,712,97,1,"[3Sum, /problems/3sum/, Medium], [4Sum, /problems/4sum/, Medium], [Two Sum II - Input array is sorted, /problems/two-sum-ii-input-array-is-sorted/, Easy], [Two Sum III - Data structure design, /problems/two-sum-iii-data-structure-design/, Easy], [Subarray Sum Equals K, /problems/subarray-sum-equals-k/, Medium], [Two Sum IV - Input is a BST, /problems/two-sum-iv-input-is-a-bst/, Easy], [Two Sum Less Than K, /problems/two-sum-less-than-k/, Easy], [Max Number of K-Sum Pairs, /problems/max-number-of-k-sum-pairs/, Medium], [Count Good Meals, /problems/count-good-meals/, Medium]"

""")

print(response.text)
