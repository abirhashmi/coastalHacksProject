from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/next')
def next():
  return render_template('nextpage.html')

@app.route('/BMI calculator')
def BMI():
  return render_template('bmi.html')


@app.route('/', methods=['POST'])
def getvalue():
  gender = request.form['gender']
  weight = request.form['weight']
  MALEpercentileDICT = {5: 136, 10: 145, 15: 153, 20: 159, 25: 165, 30: 170, 35: 175, 40: 179, 45: 184, 50: 190,
                        55: 196, 60: 201, 65: 208, 70: 215,
                        75: 222, 80: 230, 85: 241, 90: 256, 95: 284}
  FEMALEpercentileDICT = {5: 110, 10: 120, 15: 128, 20: 133, 25: 137, 30: 142, 35: 147, 40: 152, 45: 156, 50: 161,
                          55: 166, 60: 173, 65: 180, 70: 187,
                          75: 195, 80: 204, 85: 216, 90: 232, 95: 263}

  weights = list(MALEpercentileDICT.values())
  percentiles = list(MALEpercentileDICT.keys())
  weights2 = list(FEMALEpercentileDICT.values())
  percentiles2 = list(FEMALEpercentileDICT.keys())

  weight = int(weight)
  if gender == 'm':
    if weight in weights:
      print(percentiles[weights.index(weight)])
    elif weight not in weights and 136 <= weight <= 284:
      for x in weights:
        if x > weight:
          maxWeight = x
          maxWeightNum = weights.index(maxWeight)
          minWeightNum = maxWeightNum - 1
          minWeight = weights[minWeightNum]
          maxPercentile = percentiles[maxWeightNum]
          minPercentile = percentiles[minWeightNum]
          break
      formula = minPercentile + ((weight - minWeight) / (maxWeight - minWeight)) * 5
      return render_template('pass.html', f=formula)
    elif weight > 284:
      return render_template('pass.html', abovemale='Above 95th percentile')
    else:
      return render_template('pass.html', undermale='Under 5th percentile')

  if gender == 'f':
    if weight in weights2:
      print(percentiles2[weights2.index(weight)])
    elif weight not in weights2 and 110 <= weight <= 263:
      for x in weights2:
        if x > weight:
          maxWeight2 = x
          maxWeightNum2 = weights2.index(maxWeight2)
          minWeightNum2 = maxWeightNum2 - 1
          minWeight2 = weights2[minWeightNum2]
          maxPercentile2 = percentiles2[maxWeightNum2]
          minPercentile2 = percentiles2[minWeightNum2]
          break
      formula2 = minPercentile2 + ((weight - minWeight2) / (maxWeight2 - minWeight2)) * 5
      return render_template('pass.html', f2=formula2)
    elif weight > 263:
      return render_template('pass.html', abovefemale='Above 95th percentile')
    else:
      return render_template('pass.html', underfemale='Under 5th percentile')

      
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
'''
@app.route('/', methods=['POST'])
def getbmi():
  height = request.form.get('height')
  weight2 = request.form.get('weight2')
  bodymassindex = (weight2 * 703)/(height * height)
  return render_template('passbmi.html', b=bodymassindex)
'''
  #app.run(debug=True)
'''
height = request.form['height']
weight = request.form['weight2']
bmi = (weight * 703)/(height * height)
print(f"Your BMI is : {bmi}")
'''
'''
class Quiz:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "What is the healthy way to lose weight?\n(a) Going vegan\n(b)Being in a caloric deficit but still eating high protein : ",
     "What is the healthy way to gain weight?\n(a) Stuff your face with sweets\n(b)Being in a caloric surplus and eating high protein :",
]

questions = [
     Quiz(question_prompts[0], "b"),
     Quiz(question_prompts[1], "b"),
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("Having a fancy diet has no correltaion with weight. That is fine because weight loss in summary is about calories in and calories out, hence why a caloric deficit is the main idea that revolves around weight loss. As for Question #2, if you wish to gain weight the healthy weight i.e. bulking, stuffing your face with sweets will make you gain weight but not the healthy way; hence being in a caloric surplus is the best option.", score, "out of", len(questions))

run_quiz(questions)
'''
