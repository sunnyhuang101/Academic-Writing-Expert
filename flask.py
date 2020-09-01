from flask import Flask, request, render_template, redirect, url_for
import json
from interaction_pat import *
from spell import *
app = Flask(__name__)

results = []
# content = ''

# tmpcnt = 0
initial()

@app.route('/awe2', methods=['GET', 'POST']) # follow up a must-do function
def index():
    if request.method == 'GET':
        print('--- GET ---')
        global results
        print(results)
        return render_template('index.html', outputs=results)#, inputContent=content)

    return render_template('index.html')#, inputContent=content)

@app.route('/add', methods=['GET'])
def get_data_from_js():
    print('--- jsdata ---\n')
    text = request.args.get('text')
    if text == '':
        print('--- yeah ---\n')
        return redirect(url_for('index'))
    idx_hover = request.args.get('hover')
    
    print(text)
    global results
    # results.clear()

    # tmplist = []
    tmpstr = ''

    if idx_hover: # hover
        hover = idx_hover.replace('&nbsp;', ' ').strip()
        print(hover)
        tmp_spell = correction(hover)
        # tmp_spell = [('method', '', 1, 0.001776, 0.28520296296296305), ('methods', '', 2, 0.001167, 0.35650370370370377), ('mhd', '', 2, 2e-06, 0.0002824216944705339)]

        idx = text.find(hover)
        idx += len(hover)
        results_dict_h = interaction(text[:idx])
        print(text[:idx])

        if results_dict_h:
            for g, e in results_dict_h.items():
                tmpstr += ( g + ' (' + e[-1] + '%')  # add pat node
                print(g)

                full_sens_start = 0
                for i in range(len(e) - 1):
                    if (e[i] == "====="):
                        full_sens_start = i
                        break
                    print(e[i])
                    tmpstr += ('_'+e[i])

                for i in range(full_sens_start, len(e)-1):
                    print(e[i])
                    tmpstr += (e[i])


                tmpstr += '+'

            if tmpstr and tmpstr[-1]=='+':
                tmpstr = tmpstr[:-1]

            tmpstr += '+++' + tmp_spell[0][0] + '^' + tmp_spell[1][0] + '^' + tmp_spell[2][0]

            print(tmpstr)
            print('>>> hover!! <<<')
            return json.dumps(tmpstr)

    else:
        results_dict = interaction(text)
        tmp_spell = correction(text.strip().split()[-1])

        if results_dict:
            for g, e in results_dict.items():
                tmpstr += ( g + ' (' + e[-1] + '%') #tmpstr += g # add pat node
                print(g)
                full_sens_start = 0
                for i in range(len(e) - 1): #e:
                    if (e[i] == "====="):
                        full_sens_start = i
                        break
                    print(e[i])
                    tmpstr += ('_'+e[i])

                for i in range(full_sens_start, len(e)-1):
                    print(e[i])
                    tmpstr += (e[i])

                tmpstr += '+'

        # return redirect(url_for('index'))
        # print('_'.join(results))
        # return json.dumps('_'.join(results))
        if tmpstr and tmpstr[-1]=='+':
            tmpstr = tmpstr[:-1]
            
        tmpstr += '+++' + tmp_spell[0][0] + '^' + tmp_spell[1][0] + '^' + tmp_spell[2][0]
        print(tmpstr)
        return json.dumps(tmpstr)

if __name__ == '__main__':
    app.debug = True
    # app.run()
    app.run(host='0.0.0.0', port=5500, use_reloader=False) # allow public connection


# <button type="submit"></button>
# python in html -> {{username}} to pass parameter



