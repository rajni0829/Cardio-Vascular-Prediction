def tree(data,count_yes,count_no):
    if data['ca'] == 0.0:
        if data['thalach'] >= 148.0:
            if data['age'] >= 64.0:
                if data['thalach'] >= 158.0:
                    count_no+=1
                else:
                    if data['thalach'] >= 154.0:
                        count_yes+=1
                    else:
                        count_no+=1
            else:
                if data['age'] >= 41.0:
                    if data['oldpeak'] >= 0.5:
                        if data['oldpeak'] >= 0.6:
                            if data['oldpeak'] >= 1.1:
                                count_yes+=1
                            else:
                                if data['oldpeak'] >= 1.0:
                                    if data['thalach'] >= 162.0:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['age'] >= 42.0:
                            count_yes+=1
                        else:
                            if data['thalach'] >= 158.0:
                                if data['thalach'] >= 163.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                else:
                    if data['age'] >= 40.0:
                        if data['thalach'] >= 181.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_yes+=1
        else:
            if data['thalach'] >= 144.0:
                if data['oldpeak'] >= 1.8:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                if data['oldpeak'] >= 3.0:
                    count_no+=1
                else:
                    if data['thalach'] >= 111.0:
                        if data['age'] >= 58.0:
                            count_yes+=1
                        else:
                            if data['age'] >= 57.0:
                                if data['oldpeak'] >= 1.5:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                if data['oldpeak'] >= 1.8:
                                    count_no+=1
                                else:
                                    count_yes+=1
                    else:
                        if data['oldpeak'] >= 1.0:
                            count_no+=1
                        else:
                            count_yes+=1
    else:
        if data['sex'] == 0.0:
            if data['age'] >= 67.0:
                count_yes+=1
            else:
                if data['age'] >= 57.0:
                    if data['age'] >= 64.0:
                        if data['oldpeak'] >= 2.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['age'] >= 58.0:
                            count_no+=1
                        else:
                            if data['thalach'] >= 174.0:
                                count_no+=1
                            else:
                                count_yes+=1
                else:
                    count_yes+=1
        else:
            if data['thalach'] >= 173.0:
                if data['ca'] == 3.0:
                    count_yes+=1
                else:
                    if data['oldpeak'] >= 0.2:
                        if data['oldpeak'] >= 3.2:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
            else:
                if data['ca'] == 4.0:
                    if data['thalach'] >= 144.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['age'] >= 62.0:
                        if data['thalach'] >= 146.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['cp'] == 0:
        if data['sex'] == 0:
            if data['ca'] == 3:
                count_no+=1
            else:
                if data['chol'] >= 254:
                    if data['chol'] >= 307:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['chol'] >= 249:
                        count_no+=1
                    else:
                        if data['ca'] == 0:
                            if data['chol'] >= 241:
                                if data['chol'] >= 248:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
        else:
            if data['ca'] == 0:
                if data['chol'] >= 260:
                    if data['chol'] >= 270:
                        if data['chol'] >= 302:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['fbs'] == 0:
                        if data['chol'] >= 217:
                            if data['chol'] >= 228:
                                if data['chol'] >= 237:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_no+=1
                        else:
                            if data['chol'] >= 204:
                                count_yes+=1
                            else:
                                count_no+=1
                    else:
                        count_no+=1
            else:
                if data['ca'] == 3:
                    if data['fbs'] == 0:
                        count_no+=1
                    else:
                        if data['chol'] >= 289:
                            count_no+=1
                        else:
                            count_yes+=1
                else:
                    if data['chol'] >= 263:
                        if data['chol'] >= 267:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
    else:
        if data['ca'] == 2:
            if data['chol'] >= 244:
                if data['chol'] >= 319:
                    count_no+=1
                else:
                    count_yes+=1
            else:
                count_no+=1
        else:
            if data['chol'] >= 212:
                if data['chol'] >= 213:
                    if data['cp'] == 3:
                        if data['sex'] == 0:
                            count_yes+=1
                        else:
                            if data['chol'] >= 298:
                                count_yes+=1
                            else:
                                count_no+=1
                    else:
                        if data['ca'] == 1:
                            if data['chol'] >= 242:
                                if data['chol'] >= 273:
                                    count_yes+=1
                                else:
                                    if data['chol'] >= 256:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                            else:
                                count_no+=1
                        else:
                            if data['chol'] >= 274:
                                if data['chol'] >= 294:
                                    if data['sex'] == 0:
                                        count_yes+=1
                                    else:
                                        if data['cp'] == 1:
                                            count_yes+=1
                                        else:
                                            count_no+=1
                                else:
                                    count_no+=1
                            else:
                                if data['chol'] >= 232:
                                    count_yes+=1
                                else:
                                    if data['chol'] >= 231:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                else:
                    if data['fbs'] == 0:
                        count_no+=1
                    else:
                        count_yes+=1
            else:
                count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thal'] == 3.0:
        if data['oldpeak'] >= 0.8:
            if data['thalach'] >= 178.0:
                count_yes+=1
            else:
                if data['oldpeak'] >= 1.6:
                    if data['thalach'] >= 160.0:
                        count_yes+=1
                    else:
                        if data['thalach'] >= 146.0:
                            if data['age'] >= 68.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            if data['ca'] == 0.0:
                                if data['thalach'] >= 145.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_no+=1
                else:
                    count_no+=1
        else:
            if data['thalach'] >= 156.0:
                if data['age'] >= 44.0:
                    if data['age'] >= 48.0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_no+=1
            else:
                count_yes+=1
    else:
        if data['ca'] == 0.0:
            if data['age'] >= 59.0:
                if data['age'] >= 63.0:
                    if data['thalach'] >= 143.0:
                        if data['thalach'] >= 158.0:
                            if data['thalach'] >= 172.0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['oldpeak'] >= 1.5:
                            count_yes+=1
                        else:
                            count_no+=1
                else:
                    if data['sex'] == 0.0:
                        count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['thal'] == 0.0:
                    count_no+=1
                else:
                    count_yes+=1
        else:
            if data['oldpeak'] >= 0.8:
                if data['ca'] == 1.0:
                    if data['sex'] == 0.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['age'] >= 64.0:
                        count_yes+=1
                    else:
                        count_no+=1
            else:
                if data['age'] >= 48.0:
                    if data['thalach'] >= 121.0:
                        if data['age'] >= 77.0:
                            count_no+=1
                        else:
                            if data['age'] >= 63.0:
                                count_yes+=1
                            else:
                                if data['thalach'] >= 163.0:
                                    if data['age'] >= 57.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_no+=1
                    else:
                        count_no+=1
                else:
                    if data['thalach'] >= 177.0:
                        count_no+=1
                    else:
                        count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thal'] == 2:
        if data['age'] >= 59:
            if data['chol'] >= 237:
                if data['slope'] == 2:
                    if data['chol'] >= 273:
                        if data['age'] >= 65:
                            count_yes+=1
                        else:
                            if data['ca'] == 0:
                                count_no+=1
                            else:
                                count_yes+=1
                    else:
                        count_yes+=1
                else:
                    if data['chol'] >= 302:
                        if data['age'] >= 70:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
            else:
                if data['thalach'] >= 155:
                    if data['exang'] == 0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_yes+=1
        else:
            if data['thalach'] >= 122:
                if data['chol'] >= 175:
                    if data['ca'] == 1:
                        if data['thalach'] >= 174:
                            count_no+=1
                        else:
                            if data['trestbps'] >= 125:
                                count_yes+=1
                            else:
                                count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_no+=1
            else:
                count_no+=1
    else:
        if data['ca'] == 0:
            if data['exang'] == 1:
                if data['chol'] >= 270:
                    count_no+=1
                else:
                    if data['slope'] == 2:
                        count_yes+=1
                    else:
                        if data['age'] >= 57:
                            count_yes+=1
                        else:
                            count_no+=1
            else:
                if data['thalach'] >= 133:
                    if data['age'] >= 42:
                        if data['age'] >= 67:
                            if data['thalach'] >= 160:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            if data['chol'] >= 261:
                                if data['chol'] >= 263:
                                    if data['slope'] == 1:
                                        if data['age'] >= 59:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                    else:
                        count_no+=1
                else:
                    count_no+=1
        else:
            if data['trestbps'] >= 110:
                if data['thalach'] >= 173:
                    count_yes+=1
                else:
                    if data['thalach'] >= 114:
                        count_no+=1
                    else:
                        if data['age'] >= 64:
                            count_yes+=1
                        else:
                            count_no+=1
            else:
                count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thal'] == 2:
        if data['thalach'] >= 130:
            if data['thalach'] >= 157:
                if data['fbs'] == 0:
                    if data['restecg'] == 0:
                        if data['chol'] >= 330:
                            count_no+=1
                        else:
                            if data['slope'] == 1:
                                if data['chol'] >= 245:
                                    count_yes+=1
                                else:
                                    if data['thalach'] >= 175:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                            else:
                                count_yes+=1
                    else:
                        if data['thalach'] >= 163:
                            count_yes+=1
                        else:
                            if data['thalach'] >= 162:
                                if data['chol'] >= 271:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                else:
                    if data['thalach'] >= 174:
                        count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['chol'] >= 243:
                    if data['chol'] >= 256:
                        if data['thalach'] >= 152:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['thalach'] >= 138:
                        if data['thalach'] >= 155:
                            count_no+=1
                        else:
                            if data['chol'] >= 234:
                                if data['thalach'] >= 151:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                    else:
                        if data['thalach'] >= 132:
                            count_no+=1
                        else:
                            count_yes+=1
        else:
            if data['restecg'] == 0:
                if data['chol'] >= 213:
                    if data['chol'] >= 273:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_no+=1
            else:
                count_yes+=1
    else:
        if data['slope'] == 1:
            if data['thalach'] >= 109:
                if data['thalach'] >= 147:
                    if data['chol'] >= 212:
                        if data['thalach'] >= 150:
                            if data['fbs'] == 0:
                                if data['chol'] >= 229:
                                    count_no+=1
                                else:
                                    if data['thalach'] >= 155:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                            else:
                                if data['thalach'] >= 178:
                                    count_yes+=1
                                else:
                                    count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_yes+=1
                else:
                    count_no+=1
            else:
                if data['restecg'] == 0:
                    count_no+=1
                else:
                    count_yes+=1
        else:
            if data['chol'] >= 226:
                if data['chol'] >= 300:
                    count_no+=1
                else:
                    if data['thalach'] >= 158:
                        if data['thalach'] >= 165:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['fbs'] == 0:
                    if data['restecg'] == 0:
                        count_no+=1
                    else:
                        if data['chol'] >= 207:
                            if data['chol'] >= 212:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                else:
                    if data['thalach'] >= 156:
                        count_yes+=1
                    else:
                        count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['ca'] == 0.0:
        if data['oldpeak'] >= 0.2:
            if data['trestbps'] >= 120.0:
                if data['age'] >= 46.0:
                    if data['age'] >= 49.0:
                        if data['trestbps'] >= 124.0:
                            if data['fbs'] == 1.0:
                                if data['age'] >= 53.0:
                                    if data['oldpeak'] >= 1.6:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_yes+=1
                            else:
                                if data['trestbps'] >= 132.0:
                                    if data['oldpeak'] >= 2.6:
                                        count_no+=1
                                    else:
                                        if data['age'] >= 61.0:
                                            if data['trestbps'] >= 145.0:
                                                count_no+=1
                                            else:
                                                count_yes+=1
                                        else:
                                            if data['trestbps'] >= 170.0:
                                                count_no+=1
                                            else:
                                                count_yes+=1
                                else:
                                    if data['age'] >= 51.0:
                                        if data['oldpeak'] >= 1.2:
                                            count_no+=1
                                        else:
                                            if data['trestbps'] >= 130.0:
                                                count_yes+=1
                                            else:
                                                count_no+=1
                                    else:
                                        count_yes+=1
                        else:
                            if data['oldpeak'] >= 1.8:
                                if data['age'] >= 58.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_yes+=1
                    else:
                        if data['trestbps'] >= 142.0:
                            if data['trestbps'] >= 150.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                else:
                    if data['oldpeak'] >= 3.8:
                        count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['oldpeak'] >= 2.0:
                    if data['trestbps'] >= 110.0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['trestbps'] >= 118.0:
                        if data['age'] >= 39.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_yes+=1
        else:
            if data['age'] >= 63.0:
                if data['trestbps'] >= 135.0:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                if data['trestbps'] >= 152.0:
                    count_no+=1
                else:
                    count_yes+=1
    else:
        if data['age'] >= 68.0:
            count_yes+=1
        else:
            if data['ca'] == 4.0:
                if data['fbs'] == 0.0:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                if data['age'] >= 64.0:
                    if data['oldpeak'] >= 1.0:
                        if data['age'] >= 65.0:
                            count_no+=1
                        else:
                            if data['trestbps'] >= 145.0:
                                count_no+=1
                            else:
                                if data['trestbps'] >= 130.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['trestbps'] >= 110.0:
                        if data['age'] >= 52.0:
                            if data['ca'] == 3.0:
                                if data['oldpeak'] >= 1.9:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                if data['trestbps'] >= 150.0:
                                    if data['oldpeak'] >= 0.6:
                                        count_no+=1
                                    else:
                                        if data['trestbps'] >= 154.0:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                                else:
                                    count_no+=1
                        else:
                            if data['age'] >= 51.0:
                                if data['oldpeak'] >= 4.2:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_no+=1
                    else:
                        if data['age'] >= 63.0:
                            count_no+=1
                        else:
                            count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thal'] == 2.0:
        if data['oldpeak'] >= 1.8:
            if data['age'] >= 54.0:
                if data['cp'] == 3.0:
                    if data['thalach'] >= 145.0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_no+=1
            else:
                count_yes+=1
        else:
            if data['thalach'] >= 115.0:
                if data['cp'] == 3.0:
                    if data['thalach'] >= 174.0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['thalach'] >= 130.0:
                        if data['age'] >= 57.0:
                            if data['age'] >= 58.0:
                                count_yes+=1
                            else:
                                if data['thalach'] >= 164.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                        else:
                            if data['thalach'] >= 153.0:
                                count_yes+=1
                            else:
                                if data['oldpeak'] >= 0.2:
                                    count_yes+=1
                                else:
                                    count_no+=1
                    else:
                        if data['thalach'] >= 125.0:
                            if data['oldpeak'] >= 1.6:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
            else:
                count_no+=1
    else:
        if data['cp'] == 0.0:
            if data['thal'] == 1.0:
                if data['oldpeak'] >= 1.8:
                    count_no+=1
                else:
                    if data['thalach'] >= 126.0:
                        count_yes+=1
                    else:
                        count_no+=1
            else:
                if data['age'] >= 65.0:
                    if data['thalach'] >= 163.0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_no+=1
        else:
            if data['thalach'] >= 155.0:
                count_yes+=1
            else:
                if data['thalach'] >= 120.0:
                    if data['oldpeak'] >= 4.2:
                        count_yes+=1
                    else:
                        if data['oldpeak'] >= 0.3:
                            count_no+=1
                        else:
                            if data['thalach'] >= 133.0:
                                count_yes+=1
                            else:
                                count_no+=1
                else:
                    count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['cp'] == 0.0:
        if data['oldpeak'] >= 0.8:
            if data['exang'] == 0.0:
                if data['sex'] == 0.0:
                    if data['age'] >= 60.0:
                        if data['chol'] >= 394.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['age'] >= 54.0:
                        if data['age'] >= 60.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
            else:
                count_no+=1
        else:
            if data['chol'] >= 249.0:
                if data['oldpeak'] >= 0.4:
                    count_yes+=1
                else:
                    if data['chol'] >= 290.0:
                        count_no+=1
                    else:
                        if data['chol'] >= 263.0:
                            count_yes+=1
                        else:
                            count_no+=1
            else:
                if data['sex'] == 0.0:
                    count_yes+=1
                else:
                    if data['age'] >= 52.0:
                        if data['oldpeak'] >= 0.4:
                            count_yes+=1
                        else:
                            if data['exang'] == 0.0:
                                count_no+=1
                            else:
                                if data['chol'] >= 226.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                    else:
                        count_yes+=1
    else:
        if data['age'] >= 59.0:
            if data['sex'] == 1.0:
                if data['chol'] >= 246.0:
                    count_no+=1
                else:
                    if data['oldpeak'] >= 2.6:
                        count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['age'] >= 63.0:
                    count_yes+=1
                else:
                    if data['chol'] >= 318.0:
                        count_yes+=1
                    else:
                        count_no+=1
        else:
            if data['cp'] == 3.0:
                if data['chol'] >= 264.0:
                    count_no+=1
                else:
                    count_yes+=1
            else:
                if data['sex'] == 0.0:
                    count_yes+=1
                else:
                    if data['age'] >= 50.0:
                        if data['age'] >= 51.0:
                            if data['chol'] >= 261.0:
                                if data['chol'] >= 273.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                if data['oldpeak'] >= 0.2:
                                    count_yes+=1
                                else:
                                    if data['chol'] >= 232.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['slope'] == 2:
        if data['cp'] == 0:
            if data['exang'] == 0:
                if data['chol'] >= 330:
                    count_no+=1
                else:
                    if data['chol'] >= 177:
                        if data['thalach'] >= 156:
                            if data['chol'] >= 211:
                                if data['thalach'] >= 159:
                                    if data['thalach'] >= 161:
                                        count_yes+=1
                                    else:
                                        if data['chol'] >= 239:
                                            count_yes+=1
                                        else:
                                            count_no+=1
                                else:
                                    count_no+=1
                            else:
                                if data['thalach'] >= 182:
                                    count_yes+=1
                                else:
                                    count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
            else:
                if data['chol'] >= 212:
                    count_no+=1
                else:
                    if data['thalach'] >= 168:
                        count_yes+=1
                    else:
                        count_no+=1
        else:
            if data['cp'] == 3:
                if data['chol'] >= 213:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                count_yes+=1
    else:
        if data['cp'] == 0:
            if data['chol'] >= 263:
                if data['chol'] >= 269:
                    if data['exang'] == 0:
                        if data['chol'] >= 407:
                            count_no+=1
                        else:
                            if data['thalach'] >= 170:
                                count_no+=1
                            else:
                                count_yes+=1
                    else:
                        count_no+=1
                else:
                    count_yes+=1
            else:
                if data['thalach'] >= 161:
                    count_yes+=1
                else:
                    if data['thalach'] >= 148:
                        if data['thalach'] >= 154:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
        else:
            if data['chol'] >= 212:
                if data['thalach'] >= 143:
                    if data['chol'] >= 240:
                        if data['thalach'] >= 152:
                            if data['chol'] >= 284:
                                if data['chol'] >= 564:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                        else:
                            if data['thalach'] >= 146:
                                if data['chol'] >= 254:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_yes+=1
                    else:
                        if data['thalach'] >= 145:
                            if data['thalach'] >= 158:
                                if data['cp'] == 2:
                                    count_yes+=1
                                else:
                                    if data['exang'] == 0:
                                        if data['thalach'] >= 175:
                                            count_yes+=1
                                        else:
                                            count_no+=1
                                    else:
                                        count_no+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                else:
                    count_no+=1
            else:
                if data['chol'] >= 193:
                    count_yes+=1
                else:
                    if data['thalach'] >= 175:
                        count_yes+=1
                    else:
                        count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['exang'] == 0.0:
        if data['restecg'] == 0.0:
            if data['oldpeak'] >= 2.5:
                if data['thalach'] >= 154.0:
                    count_no+=1
                else:
                    count_yes+=1
            else:
                if data['sex'] == 1.0:
                    if data['thalach'] >= 173.0:
                        if data['thalach'] >= 195.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['slope'] == 0.0:
                            count_yes+=1
                        else:
                            if data['oldpeak'] >= 0.6:
                                if data['thalach'] >= 168.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                if data['thalach'] >= 158.0:
                                    if data['fbs'] == 0.0:
                                        if data['thalach'] >= 170.0:
                                            if data['thalach'] >= 171.0:
                                                count_no+=1
                                            else:
                                                count_yes+=1
                                        else:
                                            count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_yes+=1
                else:
                    if data['thalach'] >= 169.0:
                        if data['thalach'] >= 175.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1
        else:
            if data['oldpeak'] >= 3.6:
                count_no+=1
            else:
                if data['slope'] == 0.0:
                    if data['thalach'] >= 168.0:
                        if data['thalach'] >= 194.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['thalach'] >= 140.0:
                        if data['oldpeak'] >= 0.2:
                            if data['oldpeak'] >= 1.1:
                                count_yes+=1
                            else:
                                if data['oldpeak'] >= 0.8:
                                    if data['thalach'] >= 162.0:
                                        if data['thalach'] >= 178.0:
                                            count_yes+=1
                                        else:
                                            count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_yes+=1
                        else:
                            if data['thalach'] >= 161.0:
                                if data['thalach'] >= 181.0:
                                    if data['thalach'] >= 182.0:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                if data['thalach'] >= 156.0:
                                    if data['sex'] == 0.0:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    count_yes+=1
                    else:
                        if data['slope'] == 1.0:
                            if data['sex'] == 0.0:
                                if data['thalach'] >= 125.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
    else:
        if data['slope'] == 2.0:
            if data['thalach'] >= 132.0:
                if data['thalach'] >= 164.0:
                    count_yes+=1
                else:
                    if data['thalach'] >= 154.0:
                        if data['thalach'] >= 160.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
            else:
                count_yes+=1
        else:
            if data['oldpeak'] >= 1.6:
                count_no+=1
            else:
                if data['oldpeak'] >= 1.5:
                    count_yes+=1
                else:
                    if data['thalach'] >= 143.0:
                        if data['oldpeak'] >= 1.2:
                            count_yes+=1
                        else:
                            if data['oldpeak'] >= 0.1:
                                count_no+=1
                            else:
                                count_yes+=1
                    else:
                        count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['cp'] == 0.0:
        if data['trestbps'] >= 123.0:
            if data['age'] >= 59.0:
                if data['trestbps'] >= 140.0:
                    if data['chol'] >= 325.0:
                        if data['chol'] >= 407.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['age'] >= 66.0:
                            if data['oldpeak'] >= 2.3:
                                if data['chol'] >= 228.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_no+=1
                        else:
                            count_no+=1
                else:
                    if data['age'] >= 60.0:
                        if data['oldpeak'] >= 2.0:
                            if data['chol'] >= 303.0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            if data['chol'] >= 254.0:
                                count_no+=1
                            else:
                                if data['chol'] >= 209.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['age'] >= 54.0:
                    count_no+=1
                else:
                    if data['age'] >= 53.0:
                        if data['chol'] >= 282.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['age'] >= 49.0:
                            if data['age'] >= 50.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
        else:
            if data['chol'] >= 229.0:
                if data['chol'] >= 302.0:
                    if data['trestbps'] >= 115.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['age'] >= 52.0:
                        count_no+=1
                    else:
                        if data['chol'] >= 275.0:
                            count_no+=1
                        else:
                            count_yes+=1
            else:
                if data['oldpeak'] >= 2.5:
                    if data['chol'] >= 208.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['age'] >= 66.0:
                        if data['chol'] >= 223.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['chol'] >= 211.0:
                            count_yes+=1
                        else:
                            if data['chol'] >= 206.0:
                                count_no+=1
                            else:
                                count_yes+=1
    else:
        if data['oldpeak'] >= 2.5:
            if data['chol'] >= 230.0:
                count_no+=1
            else:
                count_yes+=1
        else:
            if data['trestbps'] >= 154.0:
                if data['chol'] >= 360.0:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                if data['age'] >= 56.0:
                    if data['age'] >= 58.0:
                        if data['oldpeak'] >= 1.8:
                            if data['chol'] >= 309.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            if data['age'] >= 63.0:
                                count_yes+=1
                            else:
                                if data['chol'] >= 263.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                    else:
                        if data['cp'] == 1.0:
                            count_yes+=1
                        else:
                            count_no+=1
                else:
                    if data['oldpeak'] >= 2.0:
                        count_no+=1
                    else:
                        if data['trestbps'] >= 140.0:
                            if data['oldpeak'] >= 0.8:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            if data['trestbps'] >= 110.0:
                                count_yes+=1
                            else:
                                if data['cp'] == 1.0:
                                    count_yes+=1
                                else:
                                    if data['chol'] >= 243.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['exang'] == 0:
        if data['sex'] == 0:
            if data['thal'] == 3:
                count_no+=1
            else:
                count_yes+=1
        else:
            if data['trestbps'] >= 115:
                if data['slope'] == 1:
                    if data['trestbps'] >= 160:
                        if data['chol'] >= 289:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['chol'] >= 302:
                            count_yes+=1
                        else:
                            if data['chol'] >= 233:
                                if data['chol'] >= 258:
                                    if data['chol'] >= 281:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                if data['trestbps'] >= 144:
                                    count_no+=1
                                else:
                                    if data['trestbps'] >= 130:
                                        count_yes+=1
                                    else:
                                        if data['trestbps'] >= 120:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                else:
                    if data['chol'] >= 335:
                        count_no+=1
                    else:
                        if data['trestbps'] >= 120:
                            if data['trestbps'] >= 160:
                                if data['slope'] == 0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                        else:
                            if data['chol'] >= 277:
                                count_yes+=1
                            else:
                                count_no+=1
            else:
                if data['trestbps'] >= 112:
                    if data['restecg'] == 1:
                        if data['chol'] >= 250:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_no+=1
                else:
                    if data['restecg'] == 0:
                        count_no+=1
                    else:
                        count_yes+=1
    else:
        if data['slope'] == 2:
            if data['chol'] >= 199:
                if data['chol'] >= 255:
                    if data['sex'] == 0:
                        count_yes+=1
                    else:
                        if data['trestbps'] >= 140:
                            if data['chol'] >= 299:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                else:
                    count_yes+=1
            else:
                count_no+=1
        else:
            if data['trestbps'] >= 108:
                if data['slope'] == 1:
                    if data['restecg'] == 0:
                        count_no+=1
                    else:
                        if data['chol'] >= 269:
                            count_no+=1
                        else:
                            if data['chol'] >= 263:
                                count_yes+=1
                            else:
                                count_no+=1
                else:
                    if data['thal'] == 2:
                        count_yes+=1
                    else:
                        count_no+=1
            else:
                count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['cp'] == 0:
        if data['exang'] == 1:
            if data['age'] >= 54:
                if data['trestbps'] >= 120:
                    if data['trestbps'] >= 138:
                        count_no+=1
                    else:
                        if data['trestbps'] >= 132:
                            if data['age'] >= 57:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_no+=1
                else:
                    if data['trestbps'] >= 110:
                        count_yes+=1
                    else:
                        count_no+=1
            else:
                if data['age'] >= 51:
                    if data['trestbps'] >= 142:
                        count_yes+=1
                    else:
                        if data['age'] >= 52:
                            count_no+=1
                        else:
                            count_yes+=1
                else:
                    if data['sex'] == 1:
                        count_no+=1
                    else:
                        if data['trestbps'] >= 138:
                            count_yes+=1
                        else:
                            count_no+=1
        else:
            if data['sex'] == 0:
                if data['trestbps'] >= 138:
                    if data['age'] >= 60:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['trestbps'] >= 130:
                        if data['age'] >= 61:
                            if data['age'] >= 64:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_yes+=1
            else:
                if data['age'] >= 44:
                    if data['trestbps'] >= 110:
                        if data['age'] >= 66:
                            if data['age'] >= 67:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            if data['trestbps'] >= 150:
                                count_no+=1
                            else:
                                if data['trestbps'] >= 140:
                                    count_yes+=1
                                else:
                                    if data['trestbps'] >= 115:
                                        if data['trestbps'] >= 120:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                                    else:
                                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['age'] >= 42:
                        count_yes+=1
                    else:
                        count_no+=1
    else:
        if data['sex'] == 0:
            count_yes+=1
        else:
            if data['age'] >= 56:
                if data['trestbps'] >= 130:
                    if data['cp'] == 2:
                        count_no+=1
                    else:
                        if data['age'] >= 69:
                            count_yes+=1
                        else:
                            count_no+=1
                else:
                    if data['age'] >= 58:
                        count_yes+=1
                    else:
                        if data['cp'] == 1:
                            count_no+=1
                        else:
                            count_yes+=1
            else:
                if data['cp'] == 3:
                    if data['trestbps'] >= 140:
                        count_yes+=1
                    else:
                        if data['age'] >= 38:
                            count_no+=1
                        else:
                            count_yes+=1
                else:
                    if data['trestbps'] >= 120:
                        count_yes+=1
                    else:
                        if data['trestbps'] >= 110:
                            if data['age'] >= 48:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            if data['cp'] == 1:
                                count_yes+=1
                            else:
                                if data['trestbps'] >= 108:
                                    count_no+=1
                                else:
                                    count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thal'] == 2.0:
        if data['cp'] == 0.0:
            if data['age'] >= 54.0:
                if data['restecg'] == 1.0:
                    if data['age'] >= 67.0:
                        if data['sex'] == 0.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['age'] >= 59.0:
                            if data['oldpeak'] >= 1.4:
                                count_no+=1
                            else:
                                if data['age'] >= 62.0:
                                    if data['age'] >= 63.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_no+=1
                        else:
                            count_yes+=1
                else:
                    count_no+=1
            else:
                if data['ca'] == 0.0:
                    count_yes+=1
                else:
                    count_no+=1
        else:
            if data['sex'] == 0.0:
                count_yes+=1
            else:
                if data['age'] >= 60.0:
                    count_no+=1
                else:
                    if data['age'] >= 47.0:
                        if data['age'] >= 49.0:
                            if data['ca'] == 2.0:
                                count_no+=1
                            else:
                                if data['age'] >= 58.0:
                                    if data['restecg'] == 0.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_yes+=1
                        else:
                            if data['restecg'] == 0.0:
                                count_yes+=1
                            else:
                                count_no+=1
                    else:
                        count_yes+=1
    else:
        if data['oldpeak'] >= 1.2:
            if data['thal'] == 3.0:
                if data['cp'] == 3.0:
                    if data['oldpeak'] >= 4.2:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['cp'] == 2.0:
                        if data['ca'] == 0.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_no+=1
            else:
                if data['oldpeak'] >= 1.8:
                    count_no+=1
                else:
                    count_yes+=1
        else:
            if data['cp'] == 0.0:
                if data['ca'] == 0.0:
                    if data['oldpeak'] >= 0.2:
                        count_no+=1
                    else:
                        if data['age'] >= 53.0:
                            count_yes+=1
                        else:
                            count_no+=1
                else:
                    count_no+=1
            else:
                if data['restecg'] == 1.0:
                    if data['ca'] == 3.0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['ca'] == 0.0:
                        if data['oldpeak'] >= 0.8:
                            count_no+=1
                        else:
                            if data['oldpeak'] >= 0.6:
                                count_yes+=1
                            else:
                                if data['oldpeak'] >= 0.2:
                                    count_no+=1
                                else:
                                    count_yes+=1
                    else:
                        count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['cp'] == 0.0:
        if data['ca'] == 0.0:
            if data['thal'] == 3.0:
                if data['thalach'] >= 161.0:
                    if data['chol'] >= 223.0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['oldpeak'] >= 0.8:
                        count_no+=1
                    else:
                        if data['chol'] >= 226.0:
                            count_yes+=1
                        else:
                            count_no+=1
            else:
                if data['chol'] >= 327.0:
                    count_no+=1
                else:
                    if data['thal'] == 0.0:
                        count_no+=1
                    else:
                        if data['thalach'] >= 148.0:
                            count_yes+=1
                        else:
                            if data['oldpeak'] >= 0.1:
                                count_yes+=1
                            else:
                                count_no+=1
        else:
            if data['thal'] == 2.0:
                if data['chol'] >= 303.0:
                    count_yes+=1
                else:
                    if data['slope'] == 2.0:
                        if data['ca'] == 1.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
            else:
                count_no+=1
    else:
        if data['thalach'] >= 142.0:
            if data['ca'] == 2.0:
                count_no+=1
            else:
                if data['oldpeak'] >= 3.8:
                    if data['slope'] == 0.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['ca'] == 1.0:
                        if data['slope'] == 1.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['thalach'] >= 151.0:
                            count_yes+=1
                        else:
                            if data['oldpeak'] >= 0.8:
                                if data['slope'] == 0.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
        else:
            if data['thal'] == 2.0:
                if data['chol'] >= 273.0:
                    if data['chol'] >= 275.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    count_yes+=1
            else:
                if data['chol'] >= 313.0:
                    count_yes+=1
                else:
                    count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['sex'] == 0:
        if data['ca'] == 3:
            count_no+=1
        else:
            if data['trestbps'] >= 170:
                count_no+=1
            else:
                if data['chol'] >= 236:
                    if data['chol'] >= 248:
                        if data['ca'] == 2:
                            if data['chol'] >= 303:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            if data['thalach'] >= 121:
                                if data['thalach'] >= 148:
                                    count_yes+=1
                                else:
                                    if data['chol'] >= 305:
                                        if data['ca'] == 0:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                                    else:
                                        count_yes+=1
                            else:
                                count_no+=1
                    else:
                        count_no+=1
                else:
                    if data['ca'] == 1:
                        if data['chol'] >= 205:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_yes+=1
    else:
        if data['thalach'] >= 172:
            if data['chol'] >= 233:
                count_yes+=1
            else:
                if data['chol'] >= 223:
                    count_no+=1
                else:
                    count_yes+=1
        else:
            if data['trestbps'] >= 110:
                if data['ca'] == 0:
                    if data['thalach'] >= 138:
                        if data['chol'] >= 274:
                            if data['thalach'] >= 162:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            if data['trestbps'] >= 120:
                                if data['chol'] >= 192:
                                    if data['chol'] >= 207:
                                        if data['trestbps'] >= 152:
                                            if data['chol'] >= 228:
                                                count_yes+=1
                                            else:
                                                count_no+=1
                                        else:
                                            count_yes+=1
                                    else:
                                        if data['chol'] >= 204:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                if data['thalach'] >= 168:
                                    count_no+=1
                                else:
                                    if data['chol'] >= 204:
                                        if data['trestbps'] >= 118:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                                    else:
                                        count_no+=1
                    else:
                        if data['trestbps'] >= 120:
                            if data['thalach'] >= 120:
                                count_no+=1
                            else:
                                if data['chol'] >= 270:
                                    count_no+=1
                                else:
                                    count_yes+=1
                        else:
                            if data['chol'] >= 201:
                                count_yes+=1
                            else:
                                count_no+=1
                else:
                    if data['thalach'] >= 112:
                        if data['ca'] == 4:
                            if data['chol'] >= 247:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            if data['chol'] >= 218:
                                if data['trestbps'] >= 120:
                                    count_no+=1
                                else:
                                    if data['trestbps'] >= 118:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                            else:
                                if data['chol'] >= 213:
                                    count_yes+=1
                                else:
                                    if data['trestbps'] >= 138:
                                        count_no+=1
                                    else:
                                        if data['chol'] >= 204:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                    else:
                        if data['chol'] >= 274:
                            count_no+=1
                        else:
                            count_yes+=1
            else:
                if data['trestbps'] >= 101:
                    count_yes+=1
                else:
                    count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['exang'] == 1:
        if data['thalach'] >= 163:
            if data['thalach'] >= 182:
                if data['chol'] >= 261:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                count_yes+=1
        else:
            if data['cp'] == 1:
                count_yes+=1
            else:
                if data['cp'] == 3:
                    count_yes+=1
                else:
                    if data['restecg'] == 1:
                        if data['thalach'] >= 137:
                            if data['cp'] == 0:
                                if data['chol'] >= 325:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                        else:
                            if data['thalach'] >= 112:
                                count_no+=1
                            else:
                                if data['chol'] >= 267:
                                    count_no+=1
                                else:
                                    count_yes+=1
                    else:
                        if data['thalach'] >= 148:
                            if data['chol'] >= 256:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
    else:
        if data['thalach'] >= 195:
            if data['chol'] >= 283:
                count_no+=1
            else:
                count_yes+=1
        else:
            if data['cp'] == 0:
                if data['thalach'] >= 140:
                    if data['thalach'] >= 178:
                        count_yes+=1
                    else:
                        if data['thalach'] >= 163:
                            count_no+=1
                        else:
                            if data['thalach'] >= 159:
                                if data['chol'] >= 234:
                                    if data['chol'] >= 268:
                                        if data['chol'] >= 303:
                                            count_yes+=1
                                        else:
                                            count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                if data['chol'] >= 264:
                                    count_yes+=1
                                else:
                                    if data['chol'] >= 219:
                                        if data['fbs'] == 0:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                                    else:
                                        if data['chol'] >= 177:
                                            count_yes+=1
                                        else:
                                            count_no+=1
                else:
                    if data['thalach'] >= 122:
                        if data['fbs'] == 0:
                            if data['chol'] >= 228:
                                count_yes+=1
                            else:
                                if data['chol'] >= 212:
                                    count_no+=1
                                else:
                                    count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_no+=1
            else:
                if data['thalach'] >= 156:
                    if data['thalach'] >= 165:
                        count_yes+=1
                    else:
                        if data['thalach'] >= 164:
                            count_no+=1
                        else:
                            count_yes+=1
                else:
                    if data['thalach'] >= 147:
                        if data['chol'] >= 233:
                            if data['chol'] >= 319:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            if data['chol'] >= 212:
                                count_no+=1
                            else:
                                if data['thalach'] >= 155:
                                    count_no+=1
                                else:
                                    count_yes+=1
                    else:
                        if data['thalach'] >= 115:
                            count_yes+=1
                        else:
                            count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thal'] == 2.0:
        if data['ca'] == 0.0:
            if data['oldpeak'] >= 3.4:
                count_no+=1
            else:
                if data['thalach'] >= 153.0:
                    count_yes+=1
                else:
                    if data['oldpeak'] >= 0.1:
                        count_yes+=1
                    else:
                        if data['age'] >= 47.0:
                            count_no+=1
                        else:
                            count_yes+=1
        else:
            if data['thalach'] >= 151.0:
                if data['slope'] == 2.0:
                    if data['thalach'] >= 158.0:
                        count_yes+=1
                    else:
                        if data['age'] >= 69.0:
                            count_yes+=1
                        else:
                            count_no+=1
                else:
                    if data['thalach'] >= 160.0:
                        count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['oldpeak'] >= 1.4:
                    count_yes+=1
                else:
                    count_no+=1
    else:
        if data['oldpeak'] >= 0.9:
            if data['thalach'] >= 145.0:
                if data['sex'] == 0.0:
                    count_no+=1
                else:
                    if data['age'] >= 54.0:
                        count_yes+=1
                    else:
                        if data['thalach'] >= 178.0:
                            count_yes+=1
                        else:
                            count_no+=1
            else:
                if data['thal'] == 1.0:
                    if data['oldpeak'] >= 1.8:
                        count_no+=1
                    else:
                        if data['age'] >= 59.0:
                            count_no+=1
                        else:
                            count_yes+=1
                else:
                    count_no+=1
        else:
            if data['ca'] == 0.0:
                if data['oldpeak'] >= 0.8:
                    if data['age'] >= 46.0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_yes+=1
            else:
                if data['age'] >= 51.0:
                    if data['age'] >= 57.0:
                        if data['thalach'] >= 150.0:
                            count_no+=1
                        else:
                            if data['age'] >= 58.0:
                                count_yes+=1
                            else:
                                count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['cp'] == 0.0:
        if data['oldpeak'] >= 0.8:
            if data['slope'] == 2.0:
                if data['age'] >= 51.0:
                    if data['oldpeak'] >= 2.3:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    count_yes+=1
            else:
                if data['thalach'] >= 127.0:
                    count_no+=1
                else:
                    if data['thalach'] >= 126.0:
                        if data['age'] >= 57.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_no+=1
        else:
            if data['age'] >= 67.0:
                count_no+=1
            else:
                if data['age'] >= 50.0:
                    if data['age'] >= 53.0:
                        count_yes+=1
                    else:
                        if data['thalach'] >= 160.0:
                            if data['thalach'] >= 186.0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                else:
                    if data['thalach'] >= 153.0:
                        count_no+=1
                    else:
                        if data['fbs'] == 0.0:
                            count_yes+=1
                        else:
                            count_no+=1
    else:
        if data['oldpeak'] >= 0.8:
            if data['slope'] == 1.0:
                if data['age'] >= 58.0:
                    count_no+=1
                else:
                    if data['thalach'] >= 161.0:
                        count_yes+=1
                    else:
                        count_no+=1
            else:
                if data['restecg'] == 0.0:
                    if data['age'] >= 63.0:
                        count_yes+=1
                    else:
                        if data['fbs'] == 0.0:
                            if data['cp'] == 1.0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                else:
                    count_yes+=1
        else:
            if data['thalach'] >= 195.0:
                count_no+=1
            else:
                if data['age'] >= 56.0:
                    if data['thalach'] >= 130.0:
                        if data['age'] >= 60.0:
                            count_yes+=1
                        else:
                            if data['restecg'] == 0.0:
                                if data['thalach'] >= 154.0:
                                    if data['cp'] == 3.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                    else:
                        if data['thalach'] >= 120.0:
                            count_no+=1
                        else:
                            count_yes+=1
                else:
                    count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['exang'] == 0.0:
        if data['oldpeak'] >= 2.6:
            count_no+=1
        else:
            if data['thalach'] >= 130.0:
                if data['trestbps'] >= 106.0:
                    if data['trestbps'] >= 134.0:
                        if data['trestbps'] >= 152.0:
                            if data['thalach'] >= 164.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            if data['oldpeak'] >= 0.1:
                                count_yes+=1
                            else:
                                if data['age'] >= 58.0:
                                    if data['thalach'] >= 172.0:
                                        count_yes+=1
                                    else:
                                        if data['trestbps'] >= 146.0:
                                            count_yes+=1
                                        else:
                                            count_no+=1
                                else:
                                    count_yes+=1
                    else:
                        if data['thal'] == 2.0:
                            if data['age'] >= 57.0:
                                if data['cp'] == 1.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                if data['thalach'] >= 162.0:
                                    count_yes+=1
                                else:
                                    if data['oldpeak'] >= 0.1:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                        else:
                            if data['thalach'] >= 168.0:
                                if data['thalach'] >= 173.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                if data['thalach'] >= 146.0:
                                    if data['age'] >= 57.0:
                                        if data['cp'] == 0.0:
                                            count_no+=1
                                        else:
                                            if data['oldpeak'] >= 1.0:
                                                count_yes+=1
                                            else:
                                                count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_no+=1
                else:
                    if data['cp'] == 0.0:
                        count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['oldpeak'] >= 1.0:
                    count_no+=1
                else:
                    count_yes+=1
    else:
        if data['age'] >= 74.0:
            if data['cp'] == 0.0:
                count_no+=1
            else:
                count_yes+=1
        else:
            if data['cp'] == 3.0:
                if data['thalach'] >= 182.0:
                    count_no+=1
                else:
                    count_yes+=1
            else:
                if data['thalach'] >= 148.0:
                    if data['age'] >= 53.0:
                        if data['oldpeak'] >= 1.4:
                            count_no+=1
                        else:
                            if data['oldpeak'] >= 0.6:
                                count_yes+=1
                            else:
                                count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['thalach'] >= 114.0:
                        count_no+=1
                    else:
                        if data['thalach'] >= 105.0:
                            count_yes+=1
                        else:
                            count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['ca'] == 0:
        if data['chol'] >= 229:
            if data['slope'] == 1:
                if data['chol'] >= 274:
                    if data['chol'] >= 564:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['chol'] >= 243:
                        if data['age'] >= 62:
                            count_no+=1
                        else:
                            if data['exang'] == 0:
                                count_yes+=1
                            else:
                                if data['fbs'] == 0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                    else:
                        if data['chol'] >= 237:
                            count_no+=1
                        else:
                            if data['chol'] >= 234:
                                count_yes+=1
                            else:
                                count_no+=1
            else:
                if data['age'] >= 49:
                    if data['chol'] >= 335:
                        count_no+=1
                    else:
                        if data['exang'] == 1:
                            if data['chol'] >= 325:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            if data['age'] >= 59:
                                if data['age'] >= 60:
                                    count_yes+=1
                                else:
                                    if data['chol'] >= 273:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                            else:
                                count_yes+=1
                else:
                    if data['chol'] >= 250:
                        count_yes+=1
                    else:
                        count_no+=1
        else:
            if data['chol'] >= 186:
                if data['slope'] == 0:
                    count_no+=1
                else:
                    if data['age'] >= 63:
                        if data['chol'] >= 228:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['thal'] == 3:
                            if data['chol'] >= 223:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_yes+=1
            else:
                if data['chol'] >= 185:
                    count_no+=1
                else:
                    if data['age'] >= 42:
                        count_yes+=1
                    else:
                        if data['chol'] >= 182:
                            count_yes+=1
                        else:
                            count_no+=1
    else:
        if data['thal'] == 2:
            if data['ca'] == 3:
                if data['fbs'] == 0:
                    count_no+=1
                else:
                    count_yes+=1
            else:
                if data['age'] >= 58:
                    if data['age'] >= 69:
                        count_yes+=1
                    else:
                        if data['ca'] == 2:
                            if data['age'] >= 64:
                                if data['chol'] >= 303:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_no+=1
                        else:
                            if data['chol'] >= 277:
                                count_yes+=1
                            else:
                                count_no+=1
                else:
                    if data['slope'] == 1:
                        count_no+=1
                    else:
                        if data['age'] >= 52:
                            if data['slope'] == 2:
                                if data['chol'] >= 230:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_yes+=1
                        else:
                            count_yes+=1
        else:
            if data['age'] >= 68:
                if data['ca'] == 1:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                if data['ca'] == 3:
                    if data['exang'] == 0:
                        if data['chol'] >= 407:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['ca'] == 4:
                        if data['fbs'] == 0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['age'] >= 64:
                            if data['chol'] >= 263:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['oldpeak'] >= 1.8:
        if data['age'] >= 44.0:
            count_no+=1
        else:
            if data['exang'] == 0.0:
                count_yes+=1
            else:
                count_no+=1
    else:
        if data['exang'] == 0.0:
            if data['age'] >= 57.0:
                if data['age'] >= 59.0:
                    if data['sex'] == 0.0:
                        count_yes+=1
                    else:
                        if data['thalach'] >= 158.0:
                            count_no+=1
                        else:
                            if data['thalach'] >= 143.0:
                                count_yes+=1
                            else:
                                count_no+=1
                else:
                    if data['age'] >= 58.0:
                        count_no+=1
                    else:
                        if data['thalach'] >= 159.0:
                            if data['oldpeak'] >= 0.2:
                                count_yes+=1
                            else:
                                if data['thalach'] >= 174.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                        else:
                            count_no+=1
            else:
                if data['trestbps'] >= 112.0:
                    if data['trestbps'] >= 192.0:
                        count_no+=1
                    else:
                        if data['age'] >= 51.0:
                            count_yes+=1
                        else:
                            if data['oldpeak'] >= 0.5:
                                if data['oldpeak'] >= 0.8:
                                    if data['thalach'] >= 158.0:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                else:
                    if data['age'] >= 44.0:
                        if data['thalach'] >= 152.0:
                            if data['trestbps'] >= 108.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_yes+=1
                    else:
                        count_yes+=1
        else:
            if data['trestbps'] >= 110.0:
                if data['trestbps'] >= 138.0:
                    if data['trestbps'] >= 160.0:
                        if data['oldpeak'] >= 0.8:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['thalach'] >= 164.0:
                            count_yes+=1
                        else:
                            if data['age'] >= 57.0:
                                count_no+=1
                            else:
                                count_yes+=1
                else:
                    if data['thalach'] >= 132.0:
                        if data['thalach'] >= 168.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['thalach'] >= 125.0:
                            count_yes+=1
                        else:
                            if data['oldpeak'] >= 1.0:
                                count_no+=1
                            else:
                                count_yes+=1
            else:
                count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thal'] == 2.0:
        if data['sex'] == 0.0:
            if data['oldpeak'] >= 3.4:
                count_no+=1
            else:
                if data['oldpeak'] >= 0.1:
                    if data['oldpeak'] >= 1.8:
                        if data['trestbps'] >= 130.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['trestbps'] >= 124.0:
                        if data['trestbps'] >= 135.0:
                            count_yes+=1
                        else:
                            if data['chol'] >= 303.0:
                                count_yes+=1
                            else:
                                count_no+=1
                    else:
                        count_yes+=1
        else:
            if data['trestbps'] >= 118.0:
                if data['oldpeak'] >= 2.4:
                    if data['cp'] == 2.0:
                        if data['chol'] >= 250.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_no+=1
                else:
                    if data['trestbps'] >= 160.0:
                        if data['chol'] >= 273.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['chol'] >= 237.0:
                            if data['chol'] >= 244.0:
                                if data['cp'] == 3.0:
                                    if data['chol'] >= 282.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    if data['trestbps'] >= 125.0:
                                        if data['cp'] == 0.0:
                                            if data['chol'] >= 249.0:
                                                count_no+=1
                                            else:
                                                count_yes+=1
                                        else:
                                            count_yes+=1
                                    else:
                                        count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
            else:
                if data['chol'] >= 197.0:
                    if data['cp'] == 2.0:
                        if data['chol'] >= 250.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_no+=1
                else:
                    count_yes+=1
    else:
        if data['cp'] == 0.0:
            if data['oldpeak'] >= 0.6:
                count_no+=1
            else:
                if data['chol'] >= 203.0:
                    count_no+=1
                else:
                    count_yes+=1
        else:
            if data['oldpeak'] >= 0.3:
                if data['chol'] >= 277.0:
                    if data['chol'] >= 309.0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['trestbps'] >= 170.0:
                        count_yes+=1
                    else:
                        if data['trestbps'] >= 110.0:
                            if data['chol'] >= 261.0:
                                count_no+=1
                            else:
                                if data['oldpeak'] >= 0.6:
                                    if data['oldpeak'] >= 1.4:
                                        if data['oldpeak'] >= 2.0:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    count_yes+=1
                        else:
                            count_yes+=1
            else:
                if data['trestbps'] >= 170.0:
                    count_no+=1
                else:
                    count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thalach'] >= 149:
        if data['cp'] == 0:
            if data['ca'] == 0:
                if data['thalach'] >= 157:
                    count_yes+=1
                else:
                    if data['thalach'] >= 155:
                        count_no+=1
                    else:
                        count_yes+=1
            else:
                count_no+=1
        else:
            if data['thalach'] >= 169:
                count_yes+=1
            else:
                if data['thalach'] >= 163:
                    if data['ca'] == 0:
                        if data['thalach'] >= 168:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['thalach'] >= 168:
                            count_yes+=1
                        else:
                            count_no+=1
                else:
                    if data['ca'] == 2:
                        if data['thalach'] >= 152:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['ca'] == 0:
                            if data['exang'] == 1:
                                if data['thalach'] >= 154:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                if data['thalach'] >= 158:
                                    if data['thalach'] >= 162:
                                        count_yes+=1
                                    else:
                                        if data['cp'] == 1:
                                            count_no+=1
                                        else:
                                            if data['thalach'] >= 160:
                                                count_yes+=1
                                            else:
                                                count_yes+=1
                                else:
                                    if data['thalach'] >= 155:
                                        if data['cp'] == 2:
                                            if data['thalach'] >= 157:
                                                count_yes+=1
                                            else:
                                                count_no+=1
                                        else:
                                            count_yes+=1
                                    else:
                                        count_yes+=1
                        else:
                            count_yes+=1
    else:
        if data['exang'] == 0:
            if data['ca'] == 1:
                count_no+=1
            else:
                if data['thalach'] >= 142:
                    if data['cp'] == 3:
                        count_yes+=1
                    else:
                        if data['thalach'] >= 147:
                            count_yes+=1
                        else:
                            if data['ca'] == 0:
                                count_no+=1
                            else:
                                if data['ca'] == 3:
                                    count_yes+=1
                                else:
                                    count_yes+=1
                else:
                    if data['thalach'] >= 141:
                        count_no+=1
                    else:
                        if data['thalach'] >= 116:
                            if data['cp'] == 3:
                                count_no+=1
                            else:
                                if data['thalach'] >= 128:
                                    if data['thalach'] >= 133:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    count_yes+=1
                        else:
                            if data['cp'] == 0:
                                count_no+=1
                            else:
                                count_yes+=1
        else:
            if data['ca'] == 0:
                if data['thalach'] >= 126:
                    if data['thalach'] >= 143:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['thalach'] >= 117:
                        count_no+=1
                    else:
                        count_yes+=1
            else:
                count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thal'] == 3.0:
        if data['trestbps'] >= 152.0:
            if data['oldpeak'] >= 1.2:
                if data['trestbps'] >= 180.0:
                    count_no+=1
                else:
                    count_yes+=1
            else:
                count_no+=1
        else:
            if data['trestbps'] >= 120.0:
                if data['restecg'] == 1.0:
                    if data['oldpeak'] >= 1.2:
                        if data['oldpeak'] >= 2.0:
                            count_no+=1
                        else:
                            if data['oldpeak'] >= 1.8:
                                if data['trestbps'] >= 130.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_no+=1
                    else:
                        if data['oldpeak'] >= 0.4:
                            count_yes+=1
                        else:
                            if data['trestbps'] >= 128.0:
                                if data['trestbps'] >= 140.0:
                                    if data['fbs'] == 0.0:
                                        if data['sex'] == 0.0:
                                            count_yes+=1
                                        else:
                                            count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_yes+=1
                            else:
                                count_no+=1
                else:
                    if data['trestbps'] >= 124.0:
                        count_no+=1
                    else:
                        if data['oldpeak'] >= 1.9:
                            if data['oldpeak'] >= 2.5:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
            else:
                if data['oldpeak'] >= 2.0:
                    count_no+=1
                else:
                    count_yes+=1
    else:
        if data['oldpeak'] >= 2.8:
            if data['trestbps'] >= 120.0:
                count_no+=1
            else:
                count_yes+=1
        else:
            if data['sex'] == 0.0:
                if data['trestbps'] >= 174.0:
                    count_no+=1
                else:
                    if data['trestbps'] >= 130.0:
                        if data['trestbps'] >= 132.0:
                            if data['oldpeak'] >= 1.4:
                                if data['oldpeak'] >= 1.5:
                                    count_yes+=1
                                else:
                                    if data['trestbps'] >= 150.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                            else:
                                if data['trestbps'] >= 138.0:
                                    count_yes+=1
                                else:
                                    if data['trestbps'] >= 136.0:
                                        if data['fbs'] == 0.0:
                                            count_yes+=1
                                        else:
                                            count_no+=1
                                    else:
                                        count_yes+=1
                        else:
                            if data['oldpeak'] >= 0.2:
                                count_yes+=1
                            else:
                                if data['restecg'] == 0.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                    else:
                        count_yes+=1
            else:
                if data['trestbps'] >= 115.0:
                    if data['thal'] == 2.0:
                        if data['trestbps'] >= 122.0:
                            if data['trestbps'] >= 134.0:
                                if data['trestbps'] >= 140.0:
                                    if data['trestbps'] >= 154.0:
                                        if data['trestbps'] >= 156.0:
                                            if data['fbs'] == 0.0:
                                                if data['trestbps'] >= 160.0:
                                                    count_no+=1
                                                else:
                                                    count_yes+=1
                                            else:
                                                count_yes+=1
                                        else:
                                            count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    if data['fbs'] == 0.0:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                            else:
                                if data['oldpeak'] >= 0.4:
                                    count_yes+=1
                                else:
                                    if data['trestbps'] >= 128.0:
                                        count_yes+=1
                                    else:
                                        if data['trestbps'] >= 125.0:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                        else:
                            if data['oldpeak'] >= 0.8:
                                count_no+=1
                            else:
                                count_yes+=1
                    else:
                        if data['oldpeak'] >= 2.3:
                            count_yes+=1
                        else:
                            count_no+=1
                else:
                    if data['oldpeak'] >= 1.2:
                        count_yes+=1
                    else:
                        if data['restecg'] == 1.0:
                            if data['trestbps'] >= 110.0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['exang'] == 1.0:
        if data['age'] >= 74.0:
            count_yes+=1
        else:
            if data['slope'] == 1.0:
                if data['thalach'] >= 137.0:
                    if data['chol'] >= 228.0:
                        if data['thalach'] >= 141.0:
                            if data['oldpeak'] >= 0.6:
                                count_no+=1
                            else:
                                if data['chol'] >= 309.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                        else:
                            count_yes+=1
                    else:
                        if data['oldpeak'] >= 1.2:
                            count_yes+=1
                        else:
                            count_no+=1
                else:
                    count_no+=1
            else:
                if data['sex'] == 0.0:
                    count_yes+=1
                else:
                    if data['thalach'] >= 132.0:
                        if data['thalach'] >= 164.0:
                            if data['oldpeak'] >= 1.6:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['oldpeak'] >= 5.6:
                            count_no+=1
                        else:
                            count_yes+=1
    else:
        if data['age'] >= 57.0:
            if data['age'] >= 66.0:
                if data['oldpeak'] >= 2.0:
                    if data['slope'] == 0.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['thalach'] >= 163.0:
                        if data['oldpeak'] >= 0.2:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_yes+=1
            else:
                if data['chol'] >= 229.0:
                    if data['thalach'] >= 182.0:
                        count_yes+=1
                    else:
                        if data['thalach'] >= 125.0:
                            if data['oldpeak'] >= 0.8:
                                if data['oldpeak'] >= 1.4:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                else:
                    if data['age'] >= 59.0:
                        if data['sex'] == 0.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['oldpeak'] >= 2.0:
                            count_no+=1
                        else:
                            count_yes+=1
        else:
            if data['age'] >= 44.0:
                if data['age'] >= 51.0:
                    count_yes+=1
                else:
                    if data['sex'] == 0.0:
                        count_yes+=1
                    else:
                        if data['oldpeak'] >= 0.6:
                            count_no+=1
                        else:
                            if data['thalach'] >= 156.0:
                                if data['thalach'] >= 177.0:
                                    if data['chol'] >= 222.0:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                if data['oldpeak'] >= 0.1:
                                    count_yes+=1
                                else:
                                    count_no+=1
            else:
                count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['cp'] == 0.0:
        if data['thal'] == 2.0:
            if data['chol'] >= 208.0:
                if data['oldpeak'] >= 1.4:
                    if data['age'] >= 54.0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['age'] >= 77.0:
                        count_no+=1
                    else:
                        if data['chol'] >= 234.0:
                            count_yes+=1
                        else:
                            if data['age'] >= 52.0:
                                count_no+=1
                            else:
                                count_yes+=1
            else:
                if data['oldpeak'] >= 0.1:
                    count_yes+=1
                else:
                    count_no+=1
        else:
            if data['age'] >= 66.0:
                count_yes+=1
            else:
                if data['oldpeak'] >= 0.6:
                    if data['oldpeak'] >= 1.6:
                        count_no+=1
                    else:
                        if data['oldpeak'] >= 1.5:
                            count_yes+=1
                        else:
                            count_no+=1
                else:
                    if data['oldpeak'] >= 0.2:
                        count_yes+=1
                    else:
                        if data['fbs'] == 0.0:
                            if data['age'] >= 58.0:
                                count_no+=1
                            else:
                                if data['age'] >= 53.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                        else:
                            count_yes+=1
    else:
        if data['thal'] == 3.0:
            if data['oldpeak'] >= 1.0:
                if data['chol'] >= 298.0:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                if data['age'] >= 57.0:
                    if data['age'] >= 67.0:
                        count_no+=1
                    else:
                        if data['chol'] >= 229.0:
                            if data['oldpeak'] >= 0.6:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                else:
                    count_yes+=1
        else:
            if data['chol'] >= 168.0:
                if data['chol'] >= 243.0:
                    if data['cp'] == 3.0:
                        count_no+=1
                    else:
                        if data['chol'] >= 244.0:
                            if data['cp'] == 2.0:
                                count_yes+=1
                            else:
                                if data['oldpeak'] >= 1.8:
                                    count_no+=1
                                else:
                                    count_yes+=1
                        else:
                            count_no+=1
                else:
                    count_yes+=1
            else:
                count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['cp'] == 0.0:
        if data['ca'] == 0.0:
            if data['thal'] == 2.0:
                if data['thalach'] >= 169.0:
                    if data['thalach'] >= 182.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['oldpeak'] >= 0.1:
                        count_yes+=1
                    else:
                        if data['thalach'] >= 163.0:
                            count_yes+=1
                        else:
                            count_no+=1
            else:
                if data['oldpeak'] >= 1.6:
                    count_no+=1
                else:
                    if data['thalach'] >= 166.0:
                        count_no+=1
                    else:
                        if data['thalach'] >= 161.0:
                            count_yes+=1
                        else:
                            if data['trestbps'] >= 142.0:
                                if data['oldpeak'] >= 0.8:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                if data['oldpeak'] >= 1.5:
                                    count_yes+=1
                                else:
                                    count_no+=1
        else:
            if data['thal'] == 2.0:
                if data['ca'] == 2.0:
                    if data['thalach'] >= 125.0:
                        if data['oldpeak'] >= 0.9:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_yes+=1
                else:
                    if data['trestbps'] >= 128.0:
                        if data['thalach'] >= 159.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_no+=1
            else:
                if data['thalach'] >= 109.0:
                    count_no+=1
                else:
                    if data['oldpeak'] >= 1.2:
                        count_no+=1
                    else:
                        count_yes+=1
    else:
        if data['ca'] == 3.0:
            count_no+=1
        else:
            if data['trestbps'] >= 170.0:
                count_no+=1
            else:
                if data['oldpeak'] >= 1.2:
                    if data['trestbps'] >= 130.0:
                        if data['thal'] == 3.0:
                            if data['thalach'] >= 178.0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            if data['oldpeak'] >= 3.0:
                                if data['thalach'] >= 187.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                    else:
                        if data['cp'] == 2.0:
                            if data['oldpeak'] >= 2.2:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                else:
                    if data['thalach'] >= 159.0:
                        count_yes+=1
                    else:
                        if data['thalach'] >= 158.0:
                            count_no+=1
                        else:
                            if data['trestbps'] >= 110.0:
                                count_yes+=1
                            else:
                                if data['thalach'] >= 154.0:
                                    count_yes+=1
                                else:
                                    count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['cp'] == 0.0:
        if data['oldpeak'] >= 0.1:
            if data['age'] >= 46.0:
                if data['age'] >= 71.0:
                    count_yes+=1
                else:
                    if data['slope'] == 2.0:
                        if data['sex'] == 0.0:
                            count_yes+=1
                        else:
                            if data['fbs'] == 0.0:
                                count_no+=1
                            else:
                                if data['trestbps'] >= 130.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                    else:
                        if data['sex'] == 0.0:
                            if data['trestbps'] >= 145.0:
                                count_no+=1
                            else:
                                if data['oldpeak'] >= 2.0:
                                    count_yes+=1
                                else:
                                    if data['trestbps'] >= 140.0:
                                        if data['oldpeak'] >= 1.2:
                                            count_yes+=1
                                        else:
                                            count_no+=1
                                    else:
                                        count_no+=1
                        else:
                            count_no+=1
            else:
                if data['oldpeak'] >= 1.6:
                    count_no+=1
                else:
                    count_yes+=1
        else:
            if data['age'] >= 46.0:
                if data['trestbps'] >= 122.0:
                    if data['trestbps'] >= 130.0:
                        if data['age'] >= 59.0:
                            if data['sex'] == 1.0:
                                if data['trestbps'] >= 140.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_yes+=1
                        else:
                            count_yes+=1
                    else:
                        if data['slope'] == 2.0:
                            if data['trestbps'] >= 128.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                else:
                    count_no+=1
            else:
                count_no+=1
    else:
        if data['slope'] == 1.0:
            if data['sex'] == 0.0:
                if data['age'] >= 57.0:
                    count_no+=1
                else:
                    count_yes+=1
            else:
                if data['trestbps'] >= 150.0:
                    if data['fbs'] == 0.0:
                        if data['trestbps'] >= 170.0:
                            if data['oldpeak'] >= 0.6:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['cp'] == 2.0:
                        if data['oldpeak'] >= 2.4:
                            count_yes+=1
                        else:
                            if data['age'] >= 49.0:
                                count_no+=1
                            else:
                                count_yes+=1
                    else:
                        if data['trestbps'] >= 118.0:
                            if data['trestbps'] >= 138.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
        else:
            if data['trestbps'] >= 192.0:
                count_no+=1
            else:
                if data['age'] >= 64.0:
                    if data['age'] >= 65.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['oldpeak'] >= 0.8:
                        if data['trestbps'] >= 120.0:
                            if data['age'] >= 58.0:
                                if data['trestbps'] >= 178.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['trestbps'] >= 154.0:
                            count_no+=1
                        else:
                            count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thalach'] >= 143.0:
        if data['thal'] == 3.0:
            if data['restecg'] == 0.0:
                if data['age'] >= 57.0:
                    if data['trestbps'] >= 170.0:
                        if data['oldpeak'] >= 0.6:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_no+=1
                else:
                    if data['age'] >= 54.0:
                        if data['ca'] == 0.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_no+=1
            else:
                if data['oldpeak'] >= 0.6:
                    if data['thalach'] >= 160.0:
                        if data['thalach'] >= 194.0:
                            count_yes+=1
                        else:
                            if data['trestbps'] >= 140.0:
                                if data['ca'] == 0.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['ca'] == 2.0:
                        count_no+=1
                    else:
                        count_yes+=1
        else:
            if data['oldpeak'] >= 2.6:
                count_no+=1
            else:
                if data['ca'] == 3.0:
                    count_no+=1
                else:
                    if data['trestbps'] >= 110.0:
                        if data['ca'] == 1.0:
                            if data['restecg'] == 0.0:
                                if data['trestbps'] >= 140.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                        else:
                            if data['trestbps'] >= 150.0:
                                if data['thalach'] >= 157.0:
                                    count_yes+=1
                                else:
                                    if data['oldpeak'] >= 1.4:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                            else:
                                count_yes+=1
                    else:
                        if data['restecg'] == 1.0:
                            if data['ca'] == 1.0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
    else:
        if data['age'] >= 54.0:
            if data['thalach'] >= 137.0:
                if data['oldpeak'] >= 1.2:
                    count_no+=1
                else:
                    if data['ca'] == 0.0:
                        count_yes+=1
                    else:
                        count_no+=1
            else:
                if data['trestbps'] >= 110.0:
                    if data['age'] >= 68.0:
                        if data['oldpeak'] >= 2.6:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
                else:
                    count_yes+=1
        else:
            if data['thal'] == 3.0:
                count_no+=1
            else:
                if data['trestbps'] >= 125.0:
                    count_yes+=1
                else:
                    if data['ca'] == 0.0:
                        count_yes+=1
                    else:
                        count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thal'] == 2.0:
        if data['oldpeak'] >= 2.2:
            if data['sex'] == 0.0:
                count_yes+=1
            else:
                if data['age'] >= 60.0:
                    count_no+=1
                else:
                    count_yes+=1
        else:
            if data['ca'] == 0.0:
                if data['chol'] >= 284.0:
                    if data['oldpeak'] >= 1.8:
                        count_no+=1
                    else:
                        if data['chol'] >= 330.0:
                            if data['age'] >= 61.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_yes+=1
                else:
                    if data['chol'] >= 249.0:
                        if data['chol'] >= 250.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['ca'] == 3.0:
                    count_no+=1
                else:
                    if data['age'] >= 66.0:
                        count_yes+=1
                    else:
                        if data['chol'] >= 242.0:
                            if data['oldpeak'] >= 1.0:
                                if data['chol'] >= 308.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                        else:
                            if data['chol'] >= 230.0:
                                count_no+=1
                            else:
                                if data['ca'] == 1.0:
                                    if data['sex'] == 0.0:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    count_yes+=1
    else:
        if data['oldpeak'] >= 0.6:
            if data['ca'] == 3.0:
                if data['chol'] >= 289.0:
                    count_no+=1
                else:
                    if data['oldpeak'] >= 2.0:
                        count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['chol'] >= 564.0:
                    count_yes+=1
                else:
                    if data['chol'] >= 198.0:
                        if data['oldpeak'] >= 0.8:
                            count_no+=1
                        else:
                            if data['thal'] == 1.0:
                                count_no+=1
                            else:
                                count_yes+=1
                    else:
                        if data['oldpeak'] >= 2.0:
                            count_no+=1
                        else:
                            count_yes+=1
        else:
            if data['age'] >= 43.0:
                if data['chol'] >= 229.0:
                    if data['age'] >= 45.0:
                        if data['age'] >= 64.0:
                            if data['ca'] == 2.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['ca'] == 0.0:
                            count_yes+=1
                        else:
                            count_no+=1
                else:
                    if data['age'] >= 61.0:
                        count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['thal'] == 1.0:
                    count_yes+=1
                else:
                    count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['exang'] == 0:
        if data['ca'] == 0:
            if data['trestbps'] >= 112:
                if data['thalach'] >= 114:
                    if data['thalach'] >= 148:
                        if data['thalach'] >= 162:
                            count_yes+=1
                        else:
                            if data['thalach'] >= 160:
                                if data['thal'] == 2:
                                    if data['trestbps'] >= 138:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_yes+=1
                    else:
                        if data['thalach'] >= 147:
                            if data['thal'] == 2:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            if data['thal'] == 2:
                                count_yes+=1
                            else:
                                if data['trestbps'] >= 140:
                                    if data['thalach'] >= 133:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    if data['thalach'] >= 141:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                else:
                    count_no+=1
            else:
                if data['thal'] == 2:
                    count_yes+=1
                else:
                    count_no+=1
        else:
            if data['ca'] == 4:
                count_yes+=1
            else:
                if data['thal'] == 2:
                    if data['thalach'] >= 174:
                        count_no+=1
                    else:
                        if data['trestbps'] >= 136:
                            if data['ca'] == 1:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            if data['trestbps'] >= 125:
                                count_yes+=1
                            else:
                                if data['trestbps'] >= 112:
                                    count_no+=1
                                else:
                                    count_yes+=1
                else:
                    if data['trestbps'] >= 132:
                        count_no+=1
                    else:
                        if data['thalach'] >= 146:
                            if data['ca'] == 2:
                                count_no+=1
                            else:
                                if data['ca'] == 1:
                                    if data['thalach'] >= 151:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    count_yes+=1
                        else:
                            count_no+=1
    else:
        if data['thal'] == 2:
            if data['trestbps'] >= 150:
                if data['slope'] == 1:
                    count_no+=1
                else:
                    count_yes+=1
            else:
                count_yes+=1
        else:
            if data['trestbps'] >= 110:
                if data['thal'] == 3:
                    if data['thalach'] >= 178:
                        if data['thalach'] >= 182:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['ca'] == 0:
                        count_yes+=1
                    else:
                        count_no+=1
            else:
                count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['cp'] == 0.0:
        if data['ca'] == 0.0:
            if data['oldpeak'] >= 1.8:
                count_no+=1
            else:
                if data['oldpeak'] >= 0.4:
                    if data['sex'] == 0.0:
                        count_yes+=1
                    else:
                        if data['oldpeak'] >= 0.5:
                            if data['oldpeak'] >= 1.2:
                                if data['oldpeak'] >= 1.6:
                                    count_no+=1
                                else:
                                    if data['oldpeak'] >= 1.5:
                                        count_yes+=1
                                    else:
                                        if data['trestbps'] >= 118.0:
                                            if data['trestbps'] >= 140.0:
                                                count_yes+=1
                                            else:
                                                count_no+=1
                                        else:
                                            count_yes+=1
                            else:
                                if data['oldpeak'] >= 0.8:
                                    count_no+=1
                                else:
                                    if data['trestbps'] >= 135.0:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                        else:
                            count_yes+=1
                else:
                    if data['slope'] == 1.0:
                        count_no+=1
                    else:
                        if data['trestbps'] >= 138.0:
                            count_yes+=1
                        else:
                            if data['sex'] == 0.0:
                                if data['trestbps'] >= 130.0:
                                    count_yes+=1
                                else:
                                    count_yes+=1
                            else:
                                if data['trestbps'] >= 126.0:
                                    count_no+=1
                                else:
                                    if data['trestbps'] >= 122.0:
                                        count_yes+=1
                                    else:
                                        count_no+=1
        else:
            if data['trestbps'] >= 108.0:
                if data['sex'] == 1.0:
                    count_no+=1
                else:
                    if data['trestbps'] >= 134.0:
                        count_no+=1
                    else:
                        if data['oldpeak'] >= 2.0:
                            count_yes+=1
                        else:
                            count_no+=1
            else:
                count_yes+=1
    else:
        if data['trestbps'] >= 170.0:
            if data['oldpeak'] >= 0.6:
                count_yes+=1
            else:
                count_no+=1
        else:
            if data['ca'] == 3.0:
                if data['oldpeak'] >= 1.8:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                if data['oldpeak'] >= 3.8:
                    count_no+=1
                else:
                    if data['oldpeak'] >= 1.2:
                        if data['ca'] == 1.0:
                            count_no+=1
                        else:
                            if data['trestbps'] >= 130.0:
                                count_yes+=1
                            else:
                                if data['oldpeak'] >= 1.5:
                                    if data['cp'] == 1.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_no+=1
                    else:
                        if data['ca'] == 1.0:
                            if data['cp'] == 1.0:
                                if data['slope'] == 1.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_yes+=1
                        else:
                            count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['slope'] == 2.0:
        if data['trestbps'] >= 102.0:
            if data['exang'] == 0.0:
                if data['trestbps'] >= 132.0:
                    if data['chol'] >= 203.0:
                        if data['chol'] >= 228.0:
                            if data['trestbps'] >= 154.0:
                                if data['oldpeak'] >= 2.3:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                if data['fbs'] == 0.0:
                                    count_yes+=1
                                else:
                                    if data['chol'] >= 319.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['chol'] >= 157.0:
                        if data['trestbps'] >= 115.0:
                            if data['oldpeak'] >= 0.8:
                                if data['oldpeak'] >= 1.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                        else:
                            if data['chol'] >= 198.0:
                                if data['trestbps'] >= 112.0:
                                    if data['chol'] >= 290.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_yes+=1
                            else:
                                count_no+=1
                    else:
                        count_no+=1
            else:
                if data['trestbps'] >= 132.0:
                    if data['chol'] >= 221.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['trestbps'] >= 117.0:
                        if data['chol'] >= 255.0:
                            count_no+=1
                        else:
                            if data['oldpeak'] >= 1.4:
                                count_no+=1
                            else:
                                count_yes+=1
                    else:
                        count_yes+=1
        else:
            if data['oldpeak'] >= 0.1:
                count_no+=1
            else:
                count_yes+=1
    else:
        if data['trestbps'] >= 120.0:
            if data['oldpeak'] >= 0.6:
                if data['oldpeak'] >= 4.2:
                    if data['oldpeak'] >= 5.6:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['chol'] >= 394.0:
                        count_yes+=1
                    else:
                        if data['chol'] >= 294.0:
                            if data['exang'] == 0.0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            if data['fbs'] == 0.0:
                                if data['chol'] >= 200.0:
                                    count_no+=1
                                else:
                                    if data['oldpeak'] >= 2.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                            else:
                                if data['trestbps'] >= 126.0:
                                    count_no+=1
                                else:
                                    if data['exang'] == 0.0:
                                        count_yes+=1
                                    else:
                                        count_no+=1
            else:
                if data['exang'] == 0.0:
                    if data['trestbps'] >= 125.0:
                        if data['trestbps'] >= 130.0:
                            if data['oldpeak'] >= 0.1:
                                count_yes+=1
                            else:
                                if data['trestbps'] >= 138.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['trestbps'] >= 140.0:
                        count_no+=1
                    else:
                        if data['oldpeak'] >= 0.2:
                            count_yes+=1
                        else:
                            count_no+=1
        else:
            if data['chol'] >= 219.0:
                if data['chol'] >= 303.0:
                    if data['oldpeak'] >= 4.4:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_no+=1
            else:
                if data['oldpeak'] >= 2.0:
                    if data['oldpeak'] >= 3.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thalach'] >= 152:
        if data['thalach'] >= 195:
            count_no+=1
        else:
            if data['age'] >= 60:
                if data['sex'] == 0:
                    if data['thalach'] >= 169:
                        if data['age'] >= 63:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_yes+=1
                else:
                    if data['thalach'] >= 158:
                        count_no+=1
                    else:
                        if data['age'] >= 64:
                            count_yes+=1
                        else:
                            count_no+=1
            else:
                if data['sex'] == 0:
                    count_yes+=1
                else:
                    if data['thalach'] >= 178:
                        if data['age'] >= 41:
                            count_yes+=1
                        else:
                            if data['age'] >= 40:
                                count_no+=1
                            else:
                                count_yes+=1
                    else:
                        if data['thalach'] >= 177:
                            count_no+=1
                        else:
                            if data['chol'] >= 282:
                                if data['chol'] >= 308:
                                    count_yes+=1
                                else:
                                    if data['age'] >= 51:
                                        count_no+=1
                                    else:
                                        if data['age'] >= 42:
                                            count_yes+=1
                                        else:
                                            count_no+=1
                            else:
                                if data['age'] >= 47:
                                    if data['age'] >= 49:
                                        if data['thalach'] >= 173:
                                            if data['age'] >= 58:
                                                count_no+=1
                                            else:
                                                count_yes+=1
                                        else:
                                            if data['chol'] >= 232:
                                                if data['chol'] >= 234:
                                                    count_yes+=1
                                                else:
                                                    if data['thalach'] >= 165:
                                                        count_yes+=1
                                                    else:
                                                        count_no+=1
                                            else:
                                                if data['age'] >= 59:
                                                    if data['chol'] >= 212:
                                                        count_yes+=1
                                                    else:
                                                        count_no+=1
                                                else:
                                                    if data['thalach'] >= 158:
                                                        count_yes+=1
                                                    else:
                                                        if data['thalach'] >= 156:
                                                            count_no+=1
                                                        else:
                                                            count_yes+=1
                                    else:
                                        if data['chol'] >= 257:
                                            count_yes+=1
                                        else:
                                            count_no+=1
                                else:
                                    count_yes+=1
    else:
        if data['thalach'] >= 122:
            if data['thalach'] >= 125:
                if data['thalach'] >= 142:
                    if data['chol'] >= 225:
                        if data['chol'] >= 233:
                            if data['chol'] >= 247:
                                if data['age'] >= 56:
                                    if data['thalach'] >= 145:
                                        if data['age'] >= 68:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    if data['age'] >= 51:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['chol'] >= 204:
                            count_yes+=1
                        else:
                            count_no+=1
                else:
                    if data['age'] >= 71:
                        count_yes+=1
                    else:
                        if data['restecg'] == 1:
                            if data['thalach'] >= 136:
                                if data['chol'] >= 275:
                                    count_yes+=1
                                else:
                                    if data['chol'] >= 188:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                            else:
                                if data['age'] >= 70:
                                    count_no+=1
                                else:
                                    count_yes+=1
                        else:
                            if data['thalach'] >= 138:
                                if data['age'] >= 66:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_no+=1
            else:
                count_yes+=1
        else:
            if data['age'] >= 68:
                if data['thalach'] >= 115:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                if data['age'] >= 64:
                    if data['chol'] >= 263:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['slope'] == 2:
        if data['ca'] == 0:
            if data['thalach'] >= 115:
                if data['age'] >= 64:
                    count_no+=1
                else:
                    if data['thalach'] >= 181:
                        if data['thalach'] >= 182:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['thalach'] >= 159:
                            if data['exang'] == 0:
                                count_yes+=1
                            else:
                                if data['thalach'] >= 173:
                                    count_no+=1
                                else:
                                    count_yes+=1
                        else:
                            if data['age'] >= 47:
                                count_yes+=1
                            else:
                                count_no+=1
            else:
                count_no+=1
        else:
            if data['age'] >= 44:
                if data['age'] >= 68:
                    count_yes+=1
                else:
                    if data['thalach'] >= 150:
                        if data['ca'] == 3:
                            count_yes+=1
                        else:
                            if data['ca'] == 4:
                                count_yes+=1
                            else:
                                if data['age'] >= 63:
                                    count_yes+=1
                                else:
                                    if data['thalach'] >= 160:
                                        count_no+=1
                                    else:
                                        if data['thalach'] >= 159:
                                            count_yes+=1
                                        else:
                                            count_no+=1
                    else:
                        if data['ca'] == 1:
                            count_yes+=1
                        else:
                            count_no+=1
            else:
                count_yes+=1
    else:
        if data['ca'] == 0:
            if data['exang'] == 0:
                if data['thalach'] >= 157:
                    if data['thalach'] >= 173:
                        count_yes+=1
                    else:
                        if data['age'] >= 50:
                            count_yes+=1
                        else:
                            count_no+=1
                else:
                    if data['age'] >= 41:
                        if data['thalach'] >= 150:
                            if data['age'] >= 64:
                                if data['thalach'] >= 151:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_no+=1
                        else:
                            if data['thalach'] >= 114:
                                if data['age'] >= 53:
                                    count_yes+=1
                                else:
                                    if data['age'] >= 45:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                            else:
                                count_no+=1
                    else:
                        count_no+=1
            else:
                if data['thalach'] >= 143:
                    if data['age'] >= 52:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_no+=1
        else:
            if data['age'] >= 66:
                if data['ca'] == 1:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['oldpeak'] >= 2.4:
        if data['trestbps'] >= 110.0:
            if data['cp'] == 3.0:
                count_yes+=1
            else:
                if data['trestbps'] >= 132.0:
                    count_no+=1
                else:
                    if data['oldpeak'] >= 3.5:
                        count_yes+=1
                    else:
                        count_no+=1
        else:
            count_yes+=1
    else:
        if data['sex'] == 1.0:
            if data['oldpeak'] >= 0.1:
                if data['oldpeak'] >= 2.3:
                    count_yes+=1
                else:
                    if data['trestbps'] >= 118.0:
                        if data['trestbps'] >= 134.0:
                            if data['oldpeak'] >= 0.6:
                                if data['trestbps'] >= 152.0:
                                    count_no+=1
                                else:
                                    if data['trestbps'] >= 150.0:
                                        if data['oldpeak'] >= 1.0:
                                            count_yes+=1
                                        else:
                                            count_no+=1
                                    else:
                                        if data['cp'] == 1.0:
                                            count_yes+=1
                                        else:
                                            if data['trestbps'] >= 140.0:
                                                if data['cp'] == 3.0:
                                                    count_yes+=1
                                                else:
                                                    if data['oldpeak'] >= 1.9:
                                                        count_no+=1
                                                    else:
                                                        if data['oldpeak'] >= 1.2:
                                                            count_yes+=1
                                                        else:
                                                            count_no+=1
                                            else:
                                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            if data['trestbps'] >= 124.0:
                                if data['trestbps'] >= 130.0:
                                    if data['cp'] == 2.0:
                                        if data['fbs'] == 0.0:
                                            count_yes+=1
                                        else:
                                            count_no+=1
                                    else:
                                        count_no+=1
                                else:
                                    count_no+=1
                            else:
                                if data['oldpeak'] >= 0.8:
                                    if data['fbs'] == 0.0:
                                        if data['cp'] == 1.0:
                                            if data['oldpeak'] >= 1.8:
                                                count_no+=1
                                            else:
                                                count_yes+=1
                                        else:
                                            count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_yes+=1
                    else:
                        if data['trestbps'] >= 115.0:
                            count_yes+=1
                        else:
                            if data['cp'] == 0.0:
                                count_no+=1
                            else:
                                count_yes+=1
            else:
                if data['trestbps'] >= 140.0:
                    if data['cp'] == 1.0:
                        if data['exang'] == 0.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['fbs'] == 0.0:
                            count_no+=1
                        else:
                            count_yes+=1
                else:
                    if data['cp'] == 0.0:
                        if data['trestbps'] >= 138.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['trestbps'] >= 118.0:
                            count_yes+=1
                        else:
                            if data['fbs'] == 0.0:
                                count_no+=1
                            else:
                                count_yes+=1
        else:
            if data['oldpeak'] >= 1.9:
                if data['oldpeak'] >= 2.0:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                if data['trestbps'] >= 174.0:
                    count_no+=1
                else:
                    if data['trestbps'] >= 130.0:
                        if data['trestbps'] >= 132.0:
                            if data['cp'] == 0.0:
                                if data['trestbps'] >= 140.0:
                                    if data['oldpeak'] >= 1.2:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_yes+=1
                        else:
                            if data['oldpeak'] >= 1.2:
                                count_no+=1
                            else:
                                if data['oldpeak'] >= 0.5:
                                    count_yes+=1
                                else:
                                    count_no+=1
                    else:
                        count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['oldpeak'] >= 1.9:
        if data['oldpeak'] >= 4.2:
            count_yes+=1
        else:
            if data['age'] >= 63.0:
                if data['age'] >= 69.0:
                    count_no+=1
                else:
                    if data['ca'] == 1.0:
                        count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['oldpeak'] >= 2.0:
                    count_no+=1
                else:
                    if data['chol'] >= 207.0:
                        count_no+=1
                    else:
                        count_yes+=1
    else:
        if data['exang'] == 0.0:
            if data['chol'] >= 273.0:
                if data['chol'] >= 295.0:
                    if data['oldpeak'] >= 0.2:
                        count_yes+=1
                    else:
                        if data['age'] >= 61.0:
                            count_no+=1
                        else:
                            count_yes+=1
                else:
                    if data['restecg'] == 0.0:
                        count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['ca'] == 1.0:
                    if data['chol'] >= 203.0:
                        if data['age'] >= 50.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_yes+=1
                else:
                    if data['age'] >= 41.0:
                        if data['ca'] == 3.0:
                            if data['chol'] >= 246.0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            if data['chol'] >= 249.0:
                                if data['oldpeak'] >= 0.8:
                                    if data['chol'] >= 269.0:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    if data['ca'] == 0.0:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                            else:
                                if data['ca'] == 2.0:
                                    if data['chol'] >= 223.0:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    count_yes+=1
                    else:
                        if data['chol'] >= 223.0:
                            count_no+=1
                        else:
                            count_yes+=1
        else:
            if data['chol'] >= 241.0:
                if data['slope'] == 2.0:
                    if data['restecg'] == 0.0:
                        if data['chol'] >= 282.0:
                            if data['ca'] == 1.0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
                else:
                    count_no+=1
            else:
                if data['chol'] >= 207.0:
                    if data['ca'] == 2.0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['exang'] == 0.0:
        if data['oldpeak'] >= 2.0:
            if data['thalach'] >= 168.0:
                count_yes+=1
            else:
                if data['thalach'] >= 145.0:
                    if data['sex'] == 0.0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['sex'] == 0.0:
                        count_yes+=1
                    else:
                        count_no+=1
        else:
            if data['thalach'] >= 160.0:
                if data['sex'] == 0.0:
                    count_yes+=1
                else:
                    if data['thalach'] >= 163.0:
                        if data['thalach'] >= 169.0:
                            if data['chol'] >= 300.0:
                                if data['chol'] >= 308.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                if data['chol'] >= 226.0:
                                    count_yes+=1
                                else:
                                    if data['chol'] >= 223.0:
                                        if data['thalach'] >= 181.0:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                                    else:
                                        count_yes+=1
                        else:
                            if data['chol'] >= 212.0:
                                count_no+=1
                            else:
                                count_yes+=1
                    else:
                        count_yes+=1
            else:
                if data['chol'] >= 243.0:
                    if data['sex'] == 0.0:
                        if data['thalach'] >= 122.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['oldpeak'] >= 0.2:
                            if data['chol'] >= 277.0:
                                if data['thalach'] >= 159.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                if data['chol'] >= 261.0:
                                    count_no+=1
                                else:
                                    if data['thalach'] >= 158.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                        else:
                            if data['thalach'] >= 156.0:
                                count_yes+=1
                            else:
                                count_no+=1
                else:
                    if data['thalach'] >= 150.0:
                        if data['thalach'] >= 155.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1
    else:
        if data['oldpeak'] >= 1.2:
            if data['oldpeak'] >= 1.6:
                count_no+=1
            else:
                if data['chol'] >= 230.0:
                    count_no+=1
                else:
                    count_yes+=1
        else:
            if data['thalach'] >= 152.0:
                if data['chol'] >= 207.0:
                    if data['oldpeak'] >= 1.0:
                        count_no+=1
                    else:
                        if data['chol'] >= 304.0:
                            if data['sex'] == 0.0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                else:
                    count_no+=1
            else:
                if data['chol'] >= 270.0:
                    count_no+=1
                else:
                    if data['oldpeak'] >= 0.2:
                        if data['thalach'] >= 142.0:
                            count_no+=1
                        else:
                            if data['sex'] == 0.0:
                                count_no+=1
                            else:
                                count_yes+=1
                    else:
                        if data['thalach'] >= 120.0:
                            count_no+=1
                        else:
                            count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['age'] >= 55.0:
        if data['ca'] == 0.0:
            if data['trestbps'] >= 124.0:
                if data['oldpeak'] >= 1.4:
                    count_no+=1
                else:
                    if data['oldpeak'] >= 0.6:
                        count_yes+=1
                    else:
                        if data['age'] >= 64.0:
                            count_yes+=1
                        else:
                            if data['thalach'] >= 172.0:
                                count_yes+=1
                            else:
                                if data['age'] >= 57.0:
                                    if data['fbs'] == 0.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_yes+=1
            else:
                if data['thalach'] >= 96.0:
                    if data['oldpeak'] >= 1.8:
                        if data['thalach'] >= 160.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_yes+=1
                else:
                    count_no+=1
        else:
            if data['chol'] >= 417.0:
                count_yes+=1
            else:
                if data['age'] >= 67.0:
                    if data['ca'] == 1.0:
                        if data['thalach'] >= 121.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['trestbps'] >= 120.0:
                            count_no+=1
                        else:
                            count_yes+=1
                else:
                    if data['ca'] == 4.0:
                        count_yes+=1
                    else:
                        if data['chol'] >= 303.0:
                            if data['thalach'] >= 132.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
    else:
        if data['oldpeak'] >= 0.8:
            if data['thalach'] >= 125.0:
                if data['oldpeak'] >= 1.1:
                    if data['oldpeak'] >= 1.6:
                        if data['thalach'] >= 158.0:
                            if data['thalach'] >= 173.0:
                                if data['thalach'] >= 187.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['age'] >= 43.0:
                            count_yes+=1
                        else:
                            if data['thalach'] >= 182.0:
                                count_yes+=1
                            else:
                                count_no+=1
                else:
                    if data['trestbps'] >= 134.0:
                        count_yes+=1
                    else:
                        count_no+=1
            else:
                count_no+=1
        else:
            if data['trestbps'] >= 142.0:
                if data['age'] >= 52.0:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                if data['ca'] == 1.0:
                    if data['chol'] >= 290.0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thal'] == 2.0:
        if data['oldpeak'] >= 1.9:
            if data['trestbps'] >= 134.0:
                if data['restecg'] == 1.0:
                    if data['trestbps'] >= 150.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    count_no+=1
            else:
                count_yes+=1
        else:
            if data['exang'] == 0.0:
                if data['chol'] >= 335.0:
                    if data['chol'] >= 342.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['oldpeak'] >= 0.8:
                        if data['chol'] >= 211.0:
                            if data['fbs'] == 0.0:
                                if data['oldpeak'] >= 1.8:
                                    if data['trestbps'] >= 140.0:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    if data['oldpeak'] >= 1.1:
                                        count_yes+=1
                                    else:
                                        if data['chol'] >= 237.0:
                                            if data['trestbps'] >= 120.0:
                                                count_no+=1
                                            else:
                                                count_yes+=1
                                        else:
                                            count_yes+=1
                            else:
                                if data['trestbps'] >= 150.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                        else:
                            if data['chol'] >= 204.0:
                                count_no+=1
                            else:
                                count_yes+=1
                    else:
                        if data['chol'] >= 319.0:
                            if data['fbs'] == 0.0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            if data['restecg'] == 1.0:
                                count_yes+=1
                            else:
                                if data['chol'] >= 264.0:
                                    count_yes+=1
                                else:
                                    if data['chol'] >= 236.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
            else:
                if data['trestbps'] >= 150.0:
                    count_no+=1
                else:
                    if data['chol'] >= 299.0:
                        count_no+=1
                    else:
                        if data['trestbps'] >= 132.0:
                            count_yes+=1
                        else:
                            if data['trestbps'] >= 112.0:
                                if data['chol'] >= 269.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
    else:
        if data['chol'] >= 200.0:
            if data['trestbps'] >= 100.0:
                if data['chol'] >= 564.0:
                    count_yes+=1
                else:
                    if data['chol'] >= 239.0:
                        if data['restecg'] == 1.0:
                            if data['fbs'] == 0.0:
                                if data['trestbps'] >= 130.0:
                                    count_no+=1
                                else:
                                    if data['chol'] >= 263.0:
                                        if data['chol'] >= 282.0:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                                    else:
                                        count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['oldpeak'] >= 0.9:
                            if data['thal'] == 1.0:
                                if data['fbs'] == 0.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                if data['chol'] >= 232.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                        else:
                            if data['trestbps'] >= 110.0:
                                count_yes+=1
                            else:
                                count_no+=1
            else:
                count_yes+=1
        else:
            if data['exang'] == 0.0:
                if data['oldpeak'] >= 1.4:
                    if data['chol'] >= 193.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    count_yes+=1
            else:
                if data['chol'] >= 199.0:
                    count_yes+=1
                else:
                    count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thal'] == 2:
        if data['exang'] == 1:
            if data['age'] >= 63:
                if data['age'] >= 77:
                    count_no+=1
                else:
                    if data['slope'] == 2:
                        count_yes+=1
                    else:
                        if data['restecg'] == 0:
                            if data['age'] >= 67:
                                count_no+=1
                            else:
                                if data['slope'] == 0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                        else:
                            count_no+=1
            else:
                if data['age'] >= 54:
                    if data['restecg'] == 0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_yes+=1
        else:
            if data['restecg'] == 0:
                if data['slope'] == 0:
                    count_no+=1
                else:
                    if data['age'] >= 62:
                        count_yes+=1
                    else:
                        if data['age'] >= 57:
                            if data['slope'] == 1:
                                count_yes+=1
                            else:
                                if data['age'] >= 58:
                                    count_no+=1
                                else:
                                    count_yes+=1
                        else:
                            if data['age'] >= 45:
                                count_yes+=1
                            else:
                                if data['age'] >= 44:
                                    count_no+=1
                                else:
                                    count_yes+=1
            else:
                if data['age'] >= 59:
                    if data['age'] >= 62:
                        if data['age'] >= 65:
                            count_yes+=1
                        else:
                            if data['age'] >= 64:
                                if data['slope'] == 1:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                    else:
                        if data['slope'] == 2:
                            if data['age'] >= 60:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_no+=1
                else:
                    count_yes+=1
    else:
        if data['slope'] == 2:
            if data['restecg'] == 0:
                if data['age'] >= 58:
                    count_no+=1
                else:
                    if data['age'] >= 53:
                        count_yes+=1
                    else:
                        count_no+=1
            else:
                if data['age'] >= 58:
                    if data['age'] >= 64:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['age'] >= 52:
                        if data['exang'] == 0:
                            if data['age'] >= 57:
                                count_yes+=1
                            else:
                                if data['age'] >= 54:
                                    count_yes+=1
                                else:
                                    count_yes+=1
                        else:
                            count_yes+=1
                    else:
                        count_yes+=1
        else:
            if data['exang'] == 0:
                if data['age'] >= 45:
                    if data['age'] >= 56:
                        if data['age'] >= 59:
                            if data['slope'] == 0:
                                if data['thal'] == 1:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                if data['age'] >= 67:
                                    if data['age'] >= 68:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_no+=1
                        else:
                            if data['restecg'] == 1:
                                count_yes+=1
                            else:
                                if data['age'] >= 57:
                                    count_no+=1
                                else:
                                    count_yes+=1
                    else:
                        count_no+=1
                else:
                    count_yes+=1
            else:
                if data['restecg'] == 1:
                    if data['age'] >= 57:
                        if data['age'] >= 66:
                            count_no+=1
                        else:
                            if data['thal'] == 1:
                                count_yes+=1
                            else:
                                if data['age'] >= 64:
                                    count_yes+=1
                                else:
                                    count_no+=1
                    else:
                        count_no+=1
                else:
                    count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['ca'] == 0.0:
        if data['thal'] == 3.0:
            if data['oldpeak'] >= 0.5:
                if data['thalach'] >= 154.0:
                    if data['oldpeak'] >= 0.6:
                        if data['oldpeak'] >= 3.8:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['thalach'] >= 166.0:
                            count_no+=1
                        else:
                            count_yes+=1
                else:
                    count_no+=1
            else:
                if data['thalach'] >= 147.0:
                    if data['restecg'] == 0.0:
                        if data['thalach'] >= 156.0:
                            if data['thalach'] >= 163.0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_yes+=1
                else:
                    if data['oldpeak'] >= 0.3:
                        count_no+=1
                    else:
                        count_yes+=1
        else:
            if data['restecg'] == 2.0:
                count_no+=1
            else:
                if data['thalach'] >= 170.0:
                    count_yes+=1
                else:
                    if data['oldpeak'] >= 2.8:
                        count_no+=1
                    else:
                        if data['thalach'] >= 152.0:
                            if data['thal'] == 0.0:
                                count_no+=1
                            else:
                                if data['slope'] == 2.0:
                                    if data['thalach'] >= 160.0:
                                        if data['thalach'] >= 169.0:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                                    else:
                                        if data['thalach'] >= 158.0:
                                            count_no+=1
                                        else:
                                            if data['thalach'] >= 155.0:
                                                count_yes+=1
                                            else:
                                                count_no+=1
                                else:
                                    if data['oldpeak'] >= 1.8:
                                        if data['oldpeak'] >= 2.4:
                                            count_yes+=1
                                        else:
                                            count_no+=1
                                    else:
                                        count_yes+=1
                        else:
                            if data['oldpeak'] >= 0.2:
                                count_yes+=1
                            else:
                                if data['thalach'] >= 143.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
    else:
        if data['thalach'] >= 175.0:
            count_yes+=1
        else:
            if data['oldpeak'] >= 0.6:
                if data['thal'] == 2.0:
                    if data['thalach'] >= 142.0:
                        if data['slope'] == 1.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['ca'] == 3.0:
                        if data['restecg'] == 1.0:
                            if data['oldpeak'] >= 2.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_no+=1
            else:
                if data['oldpeak'] >= 0.2:
                    if data['slope'] == 1.0:
                        if data['thalach'] >= 150.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_yes+=1
                else:
                    if data['fbs'] == 0.0:
                        if data['thalach'] >= 159.0:
                            if data['thalach'] >= 160.0:
                                if data['thalach'] >= 161.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['ca'] == 2.0:
                            count_no+=1
                        else:
                            count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thal'] == 2.0:
        if data['thalach'] >= 138.0:
            if data['thalach'] >= 157.0:
                if data['thalach'] >= 174.0:
                    if data['thalach'] >= 179.0:
                        count_yes+=1
                    else:
                        if data['thalach'] >= 177.0:
                            count_no+=1
                        else:
                            if data['age'] >= 57.0:
                                if data['oldpeak'] >= 1.6:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                else:
                    if data['sex'] == 0.0:
                        count_yes+=1
                    else:
                        if data['thalach'] >= 163.0:
                            count_yes+=1
                        else:
                            if data['oldpeak'] >= 1.6:
                                count_yes+=1
                            else:
                                if data['thalach'] >= 160.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
            else:
                if data['thalach'] >= 152.0:
                    if data['age'] >= 55.0:
                        if data['oldpeak'] >= 1.4:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['sex'] == 0.0:
                            count_yes+=1
                        else:
                            count_no+=1
                else:
                    if data['age'] >= 56.0:
                        if data['age'] >= 62.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1
        else:
            if data['exang'] == 0.0:
                if data['thalach'] >= 115.0:
                    if data['age'] >= 51.0:
                        count_yes+=1
                    else:
                        if data['thalach'] >= 126.0:
                            count_no+=1
                        else:
                            count_yes+=1
                else:
                    count_no+=1
            else:
                count_no+=1
    else:
        if data['thalach'] >= 163.0:
            if data['age'] >= 58.0:
                count_no+=1
            else:
                if data['age'] >= 54.0:
                    count_yes+=1
                else:
                    if data['age'] >= 48.0:
                        count_no+=1
                    else:
                        if data['age'] >= 40.0:
                            count_yes+=1
                        else:
                            count_no+=1
        else:
            if data['oldpeak'] >= 0.6:
                if data['thalach'] >= 150.0:
                    if data['thalach'] >= 156.0:
                        count_no+=1
                    else:
                        if data['age'] >= 58.0:
                            count_yes+=1
                        else:
                            count_no+=1
                else:
                    if data['oldpeak'] >= 4.2:
                        if data['oldpeak'] >= 5.6:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['thal'] == 1.0:
                            if data['thalach'] >= 126.0:
                                if data['thalach'] >= 146.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_no+=1
            else:
                if data['oldpeak'] >= 0.2:
                    if data['age'] >= 59.0:
                        count_yes+=1
                    else:
                        if data['thalach'] >= 147.0:
                            count_yes+=1
                        else:
                            count_no+=1
                else:
                    if data['exang'] == 1.0:
                        count_no+=1
                    else:
                        if data['thalach'] >= 158.0:
                            count_no+=1
                        else:
                            if data['age'] >= 58.0:
                                count_no+=1
                            else:
                                count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['ca'] == 0:
        if data['thal'] == 3:
            if data['cp'] == 2:
                if data['fbs'] == 0:
                    if data['restecg'] == 0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    count_no+=1
            else:
                if data['restecg'] == 0:
                    count_no+=1
                else:
                    if data['sex'] == 0:
                        count_no+=1
                    else:
                        if data['cp'] == 0:
                            count_yes+=1
                        else:
                            count_no+=1
        else:
            if data['cp'] == 0:
                if data['restecg'] == 0:
                    count_yes+=1
                else:
                    if data['sex'] == 0:
                        if data['restecg'] == 1:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['thal'] == 1:
                            count_yes+=1
                        else:
                            count_yes+=1
            else:
                if data['sex'] == 0:
                    count_yes+=1
                else:
                    if data['cp'] == 2:
                        if data['restecg'] == 0:
                            count_yes+=1
                        else:
                            if data['fbs'] == 0:
                                count_yes+=1
                            else:
                                count_yes+=1
                    else:
                        count_yes+=1
    else:
        if data['cp'] == 0:
            if data['thal'] == 2:
                if data['sex'] == 1:
                    count_no+=1
                else:
                    if data['fbs'] == 0:
                        count_yes+=1
                    else:
                        count_no+=1
            else:
                count_no+=1
        else:
            if data['thal'] == 2:
                if data['restecg'] == 0:
                    if data['cp'] == 1:
                        count_no+=1
                    else:
                        if data['ca'] == 1:
                            if data['sex'] == 0:
                                count_yes+=1
                            else:
                                if data['fbs'] == 0:
                                    count_yes+=1
                                else:
                                    count_yes+=1
                        else:
                            count_no+=1
                else:
                    if data['cp'] == 3:
                        count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['ca'] == 1:
                    if data['thal'] == 1:
                        count_no+=1
                    else:
                        if data['fbs'] == 0:
                            if data['restecg'] == 1:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                else:
                    count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thal'] == 3:
        if data['trestbps'] >= 110:
            if data['chol'] >= 200:
                if data['ca'] == 0:
                    if data['exang'] == 0:
                        if data['chol'] >= 234:
                            if data['chol'] >= 274:
                                if data['chol'] >= 313:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                if data['chol'] >= 261:
                                    if data['chol'] >= 263:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['chol'] >= 217:
                            count_no+=1
                        else:
                            if data['chol'] >= 207:
                                count_yes+=1
                            else:
                                count_no+=1
                else:
                    count_no+=1
            else:
                if data['trestbps'] >= 140:
                    if data['exang'] == 0:
                        count_yes+=1
                    else:
                        if data['chol'] >= 199:
                            count_yes+=1
                        else:
                            count_no+=1
                else:
                    if data['chol'] >= 188:
                        count_no+=1
                    else:
                        count_yes+=1
        else:
            count_yes+=1
    else:
        if data['ca'] == 0:
            if data['chol'] >= 330:
                if data['chol'] >= 342:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                if data['trestbps'] >= 110:
                    if data['chol'] >= 231:
                        if data['chol'] >= 233:
                            if data['trestbps'] >= 125:
                                count_yes+=1
                            else:
                                if data['chol'] >= 295:
                                    count_yes+=1
                                else:
                                    if data['chol'] >= 284:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['trestbps'] >= 108:
                        count_no+=1
                    else:
                        count_yes+=1
        else:
            if data['exang'] == 0:
                if data['thal'] == 1:
                    count_no+=1
                else:
                    if data['chol'] >= 319:
                        count_no+=1
                    else:
                        if data['chol'] >= 273:
                            count_yes+=1
                        else:
                            if data['chol'] >= 230:
                                if data['chol'] >= 244:
                                    if data['chol'] >= 268:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    if data['trestbps'] >= 160:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                            else:
                                count_yes+=1
            else:
                if data['chol'] >= 246:
                    count_no+=1
                else:
                    if data['chol'] >= 213:
                        count_yes+=1
                    else:
                        count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['cp'] == 0:
        if data['thal'] == 2:
            if data['ca'] == 0:
                if data['exang'] == 1:
                    if data['age'] >= 55:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['thalach'] >= 169:
                        if data['sex'] == 0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_yes+=1
            else:
                if data['sex'] == 1:
                    count_no+=1
                else:
                    if data['age'] >= 62:
                        count_no+=1
                    else:
                        count_yes+=1
        else:
            if data['thalach'] >= 161:
                if data['ca'] == 0:
                    if data['thalach'] >= 173:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_no+=1
            else:
                if data['thalach'] >= 114:
                    count_no+=1
                else:
                    if data['age'] >= 54:
                        count_no+=1
                    else:
                        count_yes+=1
    else:
        if data['ca'] == 1:
            if data['sex'] == 0:
                if data['thalach'] >= 174:
                    count_no+=1
                else:
                    count_yes+=1
            else:
                if data['age'] >= 54:
                    if data['exang'] == 0:
                        if data['age'] >= 68:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_no+=1
                else:
                    count_yes+=1
        else:
            if data['thalach'] >= 160:
                count_yes+=1
            else:
                if data['ca'] == 2:
                    if data['fbs'] == 0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['cp'] == 3:
                        count_no+=1
                    else:
                        if data['thal'] == 3:
                            if data['age'] >= 67:
                                count_no+=1
                            else:
                                if data['thalach'] >= 144:
                                    count_yes+=1
                                else:
                                    count_no+=1
                        else:
                            count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thalach'] >= 148:
        if data['chol'] >= 268:
            if data['sex'] == 0:
                if data['thalach'] >= 169:
                    if data['thalach'] >= 172:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['slope'] == 0:
                        count_no+=1
                    else:
                        if data['thalach'] >= 153:
                            count_yes+=1
                        else:
                            if data['trestbps'] >= 146:
                                count_yes+=1
                            else:
                                count_no+=1
            else:
                if data['trestbps'] >= 125:
                    count_no+=1
                else:
                    count_yes+=1
        else:
            if data['trestbps'] >= 152:
                if data['chol'] >= 227:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                if data['trestbps'] >= 115:
                    if data['slope'] == 1:
                        if data['thalach'] >= 174:
                            count_no+=1
                        else:
                            if data['chol'] >= 258:
                                count_no+=1
                            else:
                                count_yes+=1
                    else:
                        if data['trestbps'] >= 132:
                            if data['trestbps'] >= 134:
                                if data['trestbps'] >= 135:
                                    count_yes+=1
                                else:
                                    if data['chol'] >= 204:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                else:
                    if data['trestbps'] >= 112:
                        if data['chol'] >= 250:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['chol'] >= 198:
                            count_yes+=1
                        else:
                            if data['sex'] == 0:
                                count_yes+=1
                            else:
                                count_no+=1
    else:
        if data['slope'] == 2:
            if data['thalach'] >= 144:
                count_no+=1
            else:
                if data['chol'] >= 261:
                    if data['sex'] == 0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['exang'] == 0:
                        count_yes+=1
                    else:
                        if data['chol'] >= 226:
                            count_yes+=1
                        else:
                            count_no+=1
        else:
            if data['thalach'] >= 132:
                if data['thalach'] >= 139:
                    if data['exang'] == 0:
                        if data['thalach'] >= 143:
                            if data['trestbps'] >= 140:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_no+=1
                else:
                    if data['sex'] == 0:
                        if data['chol'] >= 197:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_yes+=1
            else:
                if data['sex'] == 1:
                    if data['chol'] >= 206:
                        count_no+=1
                    else:
                        if data['chol'] >= 201:
                            count_yes+=1
                        else:
                            count_no+=1
                else:
                    if data['chol'] >= 225:
                        if data['slope'] == 0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['ca'] == 0:
        if data['thal'] == 3:
            if data['slope'] == 2:
                if data['cp'] == 2:
                    count_yes+=1
                else:
                    if data['exang'] == 1:
                        count_yes+=1
                    else:
                        if data['age'] >= 57:
                            count_no+=1
                        else:
                            if data['cp'] == 0:
                                count_no+=1
                            else:
                                count_yes+=1
            else:
                if data['exang'] == 0:
                    if data['age'] >= 56:
                        if data['age'] >= 59:
                            if data['slope'] == 0:
                                count_yes+=1
                            else:
                                if data['age'] >= 67:
                                    count_yes+=1
                                else:
                                    count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
                else:
                    count_no+=1
        else:
            if data['exang'] == 0:
                if data['cp'] == 1:
                    count_yes+=1
                else:
                    if data['fbs'] == 0:
                        if data['cp'] == 3:
                            if data['age'] >= 59:
                                if data['age'] >= 60:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                        else:
                            if data['age'] >= 65:
                                count_yes+=1
                            else:
                                if data['age'] >= 64:
                                    count_no+=1
                                else:
                                    if data['age'] >= 47:
                                        count_yes+=1
                                    else:
                                        if data['age'] >= 46:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                    else:
                        count_yes+=1
            else:
                if data['cp'] == 0:
                    if data['slope'] == 2:
                        count_yes+=1
                    else:
                        if data['age'] >= 52:
                            count_no+=1
                        else:
                            if data['thal'] == 1:
                                count_no+=1
                            else:
                                count_yes+=1
                else:
                    count_yes+=1
    else:
        if data['cp'] == 2:
            if data['thal'] == 2:
                if data['ca'] == 3:
                    if data['age'] >= 53:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    count_yes+=1
            else:
                count_no+=1
        else:
            if data['age'] >= 69:
                if data['ca'] == 1:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                if data['cp'] == 3:
                    if data['age'] >= 59:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['cp'] == 0:
        if data['ca'] == 0:
            if data['thalach'] >= 161:
                count_yes+=1
            else:
                if data['age'] >= 57:
                    if data['age'] >= 59:
                        if data['age'] >= 64:
                            if data['age'] >= 67:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['sex'] == 0:
                        if data['age'] >= 55:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['age'] >= 47:
                            if data['age'] >= 50:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
        else:
            if data['sex'] == 0:
                if data['age'] >= 64:
                    if data['restecg'] == 0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_no+=1
            else:
                if data['ca'] == 3:
                    if data['fbs'] == 0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_no+=1
    else:
        if data['sex'] == 0:
            if data['ca'] == 2:
                if data['fbs'] == 0:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                count_yes+=1
        else:
            if data['age'] >= 56:
                if data['ca'] == 0:
                    if data['cp'] == 2:
                        if data['age'] >= 64:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['age'] >= 62:
                            count_yes+=1
                        else:
                            if data['age'] >= 57:
                                count_no+=1
                            else:
                                count_yes+=1
                else:
                    if data['age'] >= 68:
                        count_yes+=1
                    else:
                        if data['ca'] == 3:
                            count_yes+=1
                        else:
                            if data['age'] >= 58:
                                count_no+=1
                            else:
                                if data['age'] >= 57:
                                    count_yes+=1
                                else:
                                    count_no+=1
            else:
                if data['thalach'] >= 150:
                    if data['thalach'] >= 195:
                        count_no+=1
                    else:
                        if data['age'] >= 50:
                            count_yes+=1
                        else:
                            if data['age'] >= 47:
                                if data['thalach'] >= 175:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                else:
                    if data['age'] >= 51:
                        count_yes+=1
                    else:
                        count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thal'] == 2.0:
        if data['oldpeak'] >= 1.8:
            if data['slope'] == 2.0:
                count_yes+=1
            else:
                if data['oldpeak'] >= 2.0:
                    if data['oldpeak'] >= 3.4:
                        if data['slope'] == 0.0:
                            if data['oldpeak'] >= 3.6:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_no+=1
        else:
            if data['oldpeak'] >= 0.8:
                if data['oldpeak'] >= 1.1:
                    if data['fbs'] == 1.0:
                        if data['slope'] == 1.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['slope'] == 1.0:
                            if data['oldpeak'] >= 1.5:
                                count_yes+=1
                            else:
                                if data['oldpeak'] >= 1.4:
                                    count_no+=1
                                else:
                                    count_yes+=1
                        else:
                            count_yes+=1
                else:
                    if data['fbs'] == 0.0:
                        if data['slope'] == 1.0:
                            count_yes+=1
                        else:
                            count_yes+=1
                    else:
                        count_yes+=1
            else:
                if data['oldpeak'] >= 0.1:
                    count_yes+=1
                else:
                    if data['fbs'] == 1.0:
                        count_yes+=1
                    else:
                        if data['slope'] == 0.0:
                            count_yes+=1
                        else:
                            if data['slope'] == 2.0:
                                count_yes+=1
                            else:
                                count_yes+=1
    else:
        if data['oldpeak'] >= 0.1:
            if data['oldpeak'] >= 1.9:
                if data['slope'] == 2.0:
                    if data['thal'] == 1.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    count_no+=1
            else:
                if data['oldpeak'] >= 1.8:
                    count_yes+=1
                else:
                    if data['slope'] == 0.0:
                        if data['fbs'] == 0.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['slope'] == 1.0:
                            if data['fbs'] == 0.0:
                                if data['oldpeak'] >= 0.8:
                                    count_no+=1
                                else:
                                    if data['thal'] == 1.0:
                                        count_no+=1
                                    else:
                                        if data['oldpeak'] >= 0.6:
                                            count_yes+=1
                                        else:
                                            count_no+=1
                            else:
                                if data['oldpeak'] >= 1.2:
                                    if data['oldpeak'] >= 1.6:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_no+=1
                        else:
                            if data['oldpeak'] >= 0.2:
                                if data['oldpeak'] >= 0.6:
                                    if data['oldpeak'] >= 1.0:
                                        if data['oldpeak'] >= 1.4:
                                            if data['oldpeak'] >= 1.6:
                                                count_yes+=1
                                            else:
                                                count_no+=1
                                        else:
                                            count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    if data['oldpeak'] >= 0.3:
                                        if data['oldpeak'] >= 0.4:
                                            count_yes+=1
                                        else:
                                            count_no+=1
                                    else:
                                        count_yes+=1
                            else:
                                count_no+=1
        else:
            if data['slope'] == 1.0:
                if data['thal'] == 1.0:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                if data['fbs'] == 0.0:
                    if data['thal'] == 0.0:
                        count_yes+=1
                    else:
                        count_yes+=1
                else:
                    count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['ca'] == 0:
        if data['thalach'] >= 137:
            if data['cp'] == 0:
                if data['thalach'] >= 182:
                    count_yes+=1
                else:
                    if data['thalach'] >= 166:
                        count_no+=1
                    else:
                        if data['slope'] == 0:
                            count_no+=1
                        else:
                            if data['trestbps'] >= 150:
                                count_no+=1
                            else:
                                if data['thalach'] >= 143:
                                    count_yes+=1
                                else:
                                    count_no+=1
            else:
                if data['trestbps'] >= 180:
                    count_no+=1
                else:
                    if data['thalach'] >= 162:
                        count_yes+=1
                    else:
                        if data['cp'] == 1:
                            if data['trestbps'] >= 128:
                                count_yes+=1
                            else:
                                if data['trestbps'] >= 120:
                                    count_no+=1
                                else:
                                    count_yes+=1
                        else:
                            if data['thalach'] >= 158:
                                if data['sex'] == 0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
        else:
            if data['thalach'] >= 128:
                count_no+=1
            else:
                if data['exang'] == 0:
                    if data['thalach'] >= 115:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['thalach'] >= 126:
                        if data['trestbps'] >= 144:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['thalach'] >= 114:
                            count_no+=1
                        else:
                            count_yes+=1
    else:
        if data['cp'] == 2:
            if data['thalach'] >= 152:
                if data['slope'] == 1:
                    count_no+=1
                else:
                    count_yes+=1
            else:
                if data['trestbps'] >= 118:
                    count_no+=1
                else:
                    count_yes+=1
        else:
            if data['sex'] == 1:
                if data['ca'] == 4:
                    count_yes+=1
                else:
                    if data['thalach'] >= 178:
                        count_yes+=1
                    else:
                        if data['cp'] == 3:
                            if data['exang'] == 0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
            else:
                if data['thalach'] >= 160:
                    if data['slope'] == 2:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['exang'] == 0:
                        if data['ca'] == 3:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['oldpeak'] >= 1.8:
        if data['thalach'] >= 162.0:
            if data['thalach'] >= 173.0:
                if data['slope'] == 0.0:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                count_yes+=1
        else:
            if data['fbs'] == 0.0:
                if data['oldpeak'] >= 1.9:
                    if data['trestbps'] >= 160.0:
                        if data['slope'] == 2.0:
                            count_yes+=1
                        else:
                            if data['thalach'] >= 145.0:
                                if data['trestbps'] >= 178.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_no+=1
                    else:
                        if data['thalach'] >= 125.0:
                            count_no+=1
                        else:
                            if data['thalach'] >= 122.0:
                                if data['trestbps'] >= 140.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_no+=1
                else:
                    if data['thalach'] >= 144.0:
                        count_yes+=1
                    else:
                        count_no+=1
            else:
                count_no+=1
    else:
        if data['trestbps'] >= 142.0:
            if data['thalach'] >= 148.0:
                if data['oldpeak'] >= 0.4:
                    if data['slope'] == 2.0:
                        count_yes+=1
                    else:
                        if data['oldpeak'] >= 0.8:
                            count_no+=1
                        else:
                            count_yes+=1
                else:
                    count_no+=1
            else:
                if data['slope'] == 2.0:
                    if data['thalach'] >= 143.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    count_no+=1
        else:
            if data['oldpeak'] >= 0.8:
                if data['thalach'] >= 116.0:
                    if data['oldpeak'] >= 1.1:
                        if data['thalach'] >= 153.0:
                            if data['fbs'] == 0.0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            if data['thalach'] >= 130.0:
                                if data['slope'] == 1.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_yes+=1
                    else:
                        if data['trestbps'] >= 120.0:
                            count_no+=1
                        else:
                            count_yes+=1
                else:
                    count_no+=1
            else:
                if data['thalach'] >= 150.0:
                    if data['thalach'] >= 154.0:
                        if data['trestbps'] >= 125.0:
                            if data['trestbps'] >= 129.0:
                                if data['slope'] == 1.0:
                                    if data['thalach'] >= 175.0:
                                        count_yes+=1
                                    else:
                                        if data['thalach'] >= 163.0:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                                else:
                                    count_yes+=1
                            else:
                                count_no+=1
                        else:
                            if data['oldpeak'] >= 0.6:
                                if data['trestbps'] >= 120.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                    else:
                        if data['slope'] == 0.0:
                            count_yes+=1
                        else:
                            if data['restecg'] == 0.0:
                                count_no+=1
                            else:
                                if data['trestbps'] >= 110.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                else:
                    if data['oldpeak'] >= 0.2:
                        count_yes+=1
                    else:
                        if data['restecg'] == 1.0:
                            count_yes+=1
                        else:
                            if data['slope'] == 1.0:
                                count_no+=1
                            else:
                                count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thalach'] >= 146:
        if data['ca'] == 2:
            if data['thal'] == 2:
                if data['slope'] == 1:
                    count_no+=1
                else:
                    count_yes+=1
            else:
                count_no+=1
        else:
            if data['slope'] == 2:
                if data['thalach'] >= 195:
                    if data['thal'] == 2:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['age'] >= 37:
                        if data['ca'] == 1:
                            if data['restecg'] == 0:
                                count_no+=1
                            else:
                                if data['age'] >= 54:
                                    count_yes+=1
                                else:
                                    if data['thalach'] >= 160:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                        else:
                            count_yes+=1
                    else:
                        if data['restecg'] == 0:
                            count_no+=1
                        else:
                            count_yes+=1
            else:
                if data['thal'] == 3:
                    if data['age'] >= 59:
                        if data['ca'] == 1:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['thalach'] >= 178:
                            if data['age'] >= 42:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_no+=1
                else:
                    if data['age'] >= 57:
                        if data['thalach'] >= 154:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_yes+=1
    else:
        if data['slope'] == 2:
            if data['sex'] == 0:
                count_yes+=1
            else:
                if data['age'] >= 62:
                    if data['thalach'] >= 140:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['thalach'] >= 125:
                        count_no+=1
                    else:
                        if data['age'] >= 58:
                            count_no+=1
                        else:
                            count_yes+=1
        else:
            if data['thal'] == 2:
                if data['ca'] == 0:
                    if data['thalach'] >= 136:
                        if data['sex'] == 0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_yes+=1
                else:
                    if data['age'] >= 64:
                        if data['restecg'] == 0:
                            if data['thalach'] >= 131:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
            else:
                if data['ca'] == 4:
                    count_yes+=1
                else:
                    if data['age'] >= 64:
                        if data['thalach'] >= 112:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['thal'] == 1:
                            if data['ca'] == 0:
                                if data['slope'] == 0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['cp'] == 0.0:
        if data['ca'] == 0.0:
            if data['thal'] == 2.0:
                if data['restecg'] == 0.0:
                    if data['oldpeak'] >= 0.2:
                        count_yes+=1
                    else:
                        count_yes+=1
                else:
                    if data['slope'] == 1.0:
                        if data['oldpeak'] >= 1.6:
                            count_yes+=1
                        else:
                            if data['oldpeak'] >= 0.6:
                                if data['oldpeak'] >= 1.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['oldpeak'] >= 0.8:
                    count_no+=1
                else:
                    if data['slope'] == 1.0:
                        count_no+=1
                    else:
                        if data['restecg'] == 0.0:
                            count_yes+=1
                        else:
                            count_yes+=1
        else:
            if data['oldpeak'] >= 1.0:
                count_no+=1
            else:
                if data['restecg'] == 0.0:
                    count_no+=1
                else:
                    count_yes+=1
    else:
        if data['thal'] == 2.0:
            if data['oldpeak'] >= 3.6:
                count_no+=1
            else:
                if data['ca'] == 1.0:
                    if data['slope'] == 1.0:
                        if data['cp'] == 1.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_yes+=1
                else:
                    if data['oldpeak'] >= 0.1:
                        count_yes+=1
                    else:
                        if data['cp'] == 1.0:
                            count_yes+=1
                        else:
                            if data['restecg'] == 0.0:
                                count_yes+=1
                            else:
                                if data['ca'] == 0.0:
                                    if data['slope'] == 1.0:
                                        count_yes+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_yes+=1
        else:
            if data['ca'] == 1.0:
                if data['oldpeak'] >= 0.4:
                    count_no+=1
                else:
                    if data['restecg'] == 0.0:
                        count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['cp'] == 3.0:
                    if data['slope'] == 0.0:
                        count_yes+=1
                    else:
                        if data['oldpeak'] >= 0.2:
                            if data['oldpeak'] >= 1.9:
                                if data['restecg'] == 0.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                else:
                    if data['thal'] == 1.0:
                        count_no+=1
                    else:
                        if data['oldpeak'] >= 1.6:
                            if data['ca'] == 0.0:
                                if data['slope'] == 1.0:
                                    if data['restecg'] == 0.0:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_yes+=1
                        else:
                            if data['oldpeak'] >= 0.4:
                                count_yes+=1
                            else:
                                if data['oldpeak'] >= 0.3:
                                    count_no+=1
                                else:
                                    count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['exang'] == 0.0:
        if data['oldpeak'] >= 2.4:
            if data['trestbps'] >= 178.0:
                count_yes+=1
            else:
                count_no+=1
        else:
            if data['thalach'] >= 96.0:
                if data['thalach'] >= 166.0:
                    if data['thalach'] >= 172.0:
                        if data['trestbps'] >= 152.0:
                            if data['fbs'] == 0.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            if data['slope'] == 1.0:
                                if data['thalach'] >= 175.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                    else:
                        if data['restecg'] == 0.0:
                            if data['oldpeak'] >= 2.0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            if data['thalach'] >= 169.0:
                                count_yes+=1
                            else:
                                if data['sex'] == 0.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                else:
                    if data['trestbps'] >= 102.0:
                        if data['trestbps'] >= 160.0:
                            if data['thalach'] >= 138.0:
                                if data['oldpeak'] >= 0.4:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_no+=1
                        else:
                            if data['oldpeak'] >= 1.9:
                                if data['thalach'] >= 162.0:
                                    count_yes+=1
                                else:
                                    if data['fbs'] == 0.0:
                                        if data['sex'] == 0.0:
                                            count_yes+=1
                                        else:
                                            count_no+=1
                                    else:
                                        count_no+=1
                            else:
                                if data['sex'] == 0.0:
                                    count_yes+=1
                                else:
                                    if data['oldpeak'] >= 0.6:
                                        if data['slope'] == 1.0:
                                            if data['oldpeak'] >= 1.8:
                                                count_yes+=1
                                            else:
                                                count_no+=1
                                        else:
                                            if data['thalach'] >= 151.0:
                                                count_yes+=1
                                            else:
                                                if data['thalach'] >= 144.0:
                                                    count_no+=1
                                                else:
                                                    count_yes+=1
                                    else:
                                        count_yes+=1
                    else:
                        count_no+=1
            else:
                count_no+=1
    else:
        if data['thalach'] >= 164.0:
            if data['oldpeak'] >= 1.0:
                if data['thalach'] >= 178.0:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                count_yes+=1
        else:
            if data['trestbps'] >= 110.0:
                if data['thalach'] >= 152.0:
                    if data['sex'] == 0.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['slope'] == 2.0:
                        if data['thalach'] >= 144.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['restecg'] == 1.0:
                            if data['fbs'] == 0.0:
                                if data['trestbps'] >= 120.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_yes+=1
                        else:
                            if data['thalach'] >= 144.0:
                                if data['thalach'] >= 146.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_no+=1
            else:
                if data['thalach'] >= 143.0:
                    count_yes+=1
                else:
                    count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['cp'] == 0:
        if data['thal'] == 2:
            if data['thalach'] >= 143:
                if data['chol'] >= 204:
                    if data['trestbps'] >= 174:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['thalach'] >= 182:
                        count_yes+=1
                    else:
                        count_no+=1
            else:
                if data['chol'] >= 303:
                    count_yes+=1
                else:
                    count_no+=1
        else:
            if data['trestbps'] >= 110:
                if data['thalach'] >= 111:
                    if data['slope'] == 2:
                        if data['trestbps'] >= 117:
                            if data['thalach'] >= 144:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_yes+=1
                    else:
                        if data['thal'] == 3:
                            count_no+=1
                        else:
                            if data['thalach'] >= 148:
                                count_yes+=1
                            else:
                                count_no+=1
                else:
                    if data['thalach'] >= 105:
                        count_yes+=1
                    else:
                        count_no+=1
            else:
                count_yes+=1
    else:
        if data['slope'] == 1:
            if data['thal'] == 2:
                if data['thalach'] >= 174:
                    if data['thalach'] >= 175:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['trestbps'] >= 135:
                        count_yes+=1
                    else:
                        if data['trestbps'] >= 134:
                            count_no+=1
                        else:
                            count_yes+=1
            else:
                if data['cp'] == 2:
                    if data['thalach'] >= 147:
                        if data['thalach'] >= 165:
                            count_no+=1
                        else:
                            if data['trestbps'] >= 180:
                                count_no+=1
                            else:
                                count_yes+=1
                    else:
                        count_no+=1
                else:
                    count_yes+=1
        else:
            if data['trestbps'] >= 112:
                count_yes+=1
            else:
                if data['slope'] == 0:
                    count_no+=1
                else:
                    if data['thalach'] >= 153:
                        count_yes+=1
                    else:
                        if data['thalach'] >= 152:
                            count_no+=1
                        else:
                            count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['ca'] == 0:
        if data['thal'] == 3:
            if data['age'] >= 52:
                if data['thalach'] >= 133:
                    if data['thalach'] >= 159:
                        if data['thalach'] >= 160:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['age'] >= 57:
                        count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['age'] >= 44:
                    if data['age'] >= 46:
                        if data['fbs'] == 0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_yes+=1
                else:
                    count_no+=1
        else:
            if data['age'] >= 58:
                if data['thalach'] >= 160:
                    if data['age'] >= 62:
                        count_yes+=1
                    else:
                        if data['fbs'] == 0:
                            count_no+=1
                        else:
                            count_yes+=1
                else:
                    if data['age'] >= 60:
                        count_yes+=1
                    else:
                        if data['age'] >= 59:
                            count_no+=1
                        else:
                            count_yes+=1
            else:
                if data['thalach'] >= 153:
                    count_yes+=1
                else:
                    if data['thalach'] >= 152:
                        if data['age'] >= 47:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_yes+=1
    else:
        if data['sex'] == 1:
            if data['thalach'] >= 173:
                if data['age'] >= 54:
                    count_no+=1
                else:
                    count_yes+=1
            else:
                if data['age'] >= 69:
                    if data['thal'] == 2:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['age'] >= 44:
                        if data['age'] >= 68:
                            if data['thalach'] >= 151:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            if data['age'] >= 57:
                                count_no+=1
                            else:
                                if data['age'] >= 51:
                                    if data['thal'] == 2:
                                        if data['thalach'] >= 125:
                                            count_yes+=1
                                        else:
                                            count_no+=1
                                    else:
                                        count_no+=1
                                else:
                                    count_no+=1
                    else:
                        count_yes+=1
        else:
            if data['thal'] == 2:
                if data['ca'] == 2:
                    if data['age'] >= 71:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['thalach'] >= 174:
                        count_no+=1
                    else:
                        count_yes+=1
            else:
                count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thalach'] >= 147:
        if data['cp'] == 0:
            if data['thalach'] >= 156:
                if data['thalach'] >= 163:
                    if data['sex'] == 0:
                        count_yes+=1
                    else:
                        if data['thalach'] >= 186:
                            count_yes+=1
                        else:
                            count_no+=1
                else:
                    if data['chol'] >= 394:
                        count_yes+=1
                    else:
                        if data['restecg'] == 0:
                            count_no+=1
                        else:
                            if data['chol'] >= 234:
                                if data['trestbps'] >= 135:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_no+=1
            else:
                if data['thalach'] >= 150:
                    if data['chol'] >= 302:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    count_yes+=1
        else:
            if data['thalach'] >= 169:
                if data['restecg'] == 0:
                    if data['trestbps'] >= 138:
                        count_no+=1
                    else:
                        if data['cp'] == 1:
                            if data['thalach'] >= 175:
                                count_yes+=1
                            else:
                                if data['trestbps'] >= 130:
                                    count_no+=1
                                else:
                                    count_yes+=1
                        else:
                            count_yes+=1
                else:
                    count_yes+=1
            else:
                if data['sex'] == 0:
                    count_yes+=1
                else:
                    if data['restecg'] == 0:
                        if data['trestbps'] >= 152:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['thalach'] >= 152:
                            if data['trestbps'] >= 150:
                                count_yes+=1
                            else:
                                if data['cp'] == 1:
                                    if data['thalach'] >= 168:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    if data['trestbps'] >= 140:
                                        count_no+=1
                                    else:
                                        if data['trestbps'] >= 130:
                                            count_yes+=1
                                        else:
                                            count_no+=1
                        else:
                            count_yes+=1
    else:
        if data['cp'] == 0:
            if data['trestbps'] >= 110:
                if data['chol'] >= 164:
                    if data['trestbps'] >= 132:
                        if data['thalach'] >= 114:
                            count_no+=1
                        else:
                            if data['restecg'] == 0:
                                count_yes+=1
                            else:
                                count_no+=1
                    else:
                        if data['trestbps'] >= 128:
                            if data['thalach'] >= 130:
                                if data['thalach'] >= 143:
                                    if data['thalach'] >= 144:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                if data['restecg'] == 0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                        else:
                            if data['thalach'] >= 143:
                                if data['trestbps'] >= 120:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                if data['thalach'] >= 140:
                                    if data['chol'] >= 258:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_no+=1
                else:
                    if data['trestbps'] >= 130:
                        count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['trestbps'] >= 106:
                    count_yes+=1
                else:
                    count_no+=1
        else:
            if data['thalach'] >= 121:
                if data['sex'] == 0:
                    count_yes+=1
                else:
                    if data['chol'] >= 256:
                        count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['chol'] >= 246:
                    count_no+=1
                else:
                    count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['cp'] == 0:
        if data['sex'] == 1:
            if data['thalach'] >= 178:
                count_yes+=1
            else:
                if data['trestbps'] >= 142:
                    if data['trestbps'] >= 145:
                        if data['thalach'] >= 171:
                            count_yes+=1
                        else:
                            if data['chol'] >= 276:
                                count_no+=1
                            else:
                                if data['thalach'] >= 138:
                                    count_yes+=1
                                else:
                                    count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['trestbps'] >= 128:
                        if data['trestbps'] >= 130:
                            if data['exang'] == 0:
                                if data['chol'] >= 254:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_no+=1
                        else:
                            if data['thalach'] >= 161:
                                count_no+=1
                            else:
                                count_yes+=1
                    else:
                        count_no+=1
        else:
            if data['thalach'] >= 152:
                if data['thalach'] >= 169:
                    count_no+=1
                else:
                    count_yes+=1
            else:
                if data['trestbps'] >= 124:
                    if data['chol'] >= 205:
                        count_no+=1
                    else:
                        if data['trestbps'] >= 130:
                            count_yes+=1
                        else:
                            count_no+=1
                else:
                    count_yes+=1
    else:
        if data['thalach'] >= 133:
            if data['trestbps'] >= 180:
                count_no+=1
            else:
                if data['thalach'] >= 174:
                    if data['sex'] == 0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['thalach'] >= 153:
                        if data['cp'] == 3:
                            if data['trestbps'] >= 134:
                                if data['trestbps'] >= 150:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                        else:
                            if data['thalach'] >= 173:
                                if data['chol'] >= 224:
                                    if data['trestbps'] >= 132:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_yes+=1
                            else:
                                if data['trestbps'] >= 120:
                                    count_yes+=1
                                else:
                                    if data['trestbps'] >= 112:
                                        if data['sex'] == 0:
                                            count_yes+=1
                                        else:
                                            count_no+=1
                                    else:
                                        count_yes+=1
                    else:
                        if data['thalach'] >= 150:
                            if data['trestbps'] >= 152:
                                count_no+=1
                            else:
                                if data['trestbps'] >= 138:
                                    count_yes+=1
                                else:
                                    if data['chol'] >= 229:
                                        if data['trestbps'] >= 128:
                                            count_no+=1
                                        else:
                                            if data['trestbps'] >= 118:
                                                count_yes+=1
                                            else:
                                                count_no+=1
                                    else:
                                        count_yes+=1
                        else:
                            if data['trestbps'] >= 150:
                                if data['trestbps'] >= 156:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
        else:
            if data['sex'] == 0:
                count_yes+=1
            else:
                if data['chol'] >= 264:
                    count_no+=1
                else:
                    if data['chol'] >= 175:
                        count_yes+=1
                    else:
                        count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thal'] == 2:
        if data['exang'] == 1:
            if data['age'] >= 55:
                if data['slope'] == 2:
                    if data['thalach'] >= 162:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['thalach'] >= 137:
                        if data['thalach'] >= 143:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
            else:
                count_yes+=1
        else:
            if data['thalach'] >= 163:
                if data['trestbps'] >= 112:
                    count_yes+=1
                else:
                    if data['thalach'] >= 177:
                        count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['chol'] >= 235:
                    if data['chol'] >= 319:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['thalach'] >= 160:
                        count_no+=1
                    else:
                        if data['chol'] >= 234:
                            if data['thalach'] >= 145:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_yes+=1
    else:
        if data['thalach'] >= 144:
            if data['trestbps'] >= 126:
                if data['trestbps'] >= 172:
                    if data['thalach'] >= 165:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['thal'] == 1:
                        count_yes+=1
                    else:
                        if data['chol'] >= 164:
                            if data['thalach'] >= 161:
                                if data['chol'] >= 223:
                                    if data['thalach'] >= 170:
                                        count_no+=1
                                    else:
                                        if data['age'] >= 54:
                                            count_yes+=1
                                        else:
                                            count_no+=1
                                else:
                                    if data['thalach'] >= 163:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                            else:
                                if data['trestbps'] >= 170:
                                    if data['thalach'] >= 159:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_no+=1
                        else:
                            count_yes+=1
            else:
                if data['thalach'] >= 156:
                    if data['age'] >= 58:
                        count_no+=1
                    else:
                        if data['thalach'] >= 166:
                            if data['thalach'] >= 173:
                                if data['exang'] == 0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                else:
                    count_yes+=1
        else:
            if data['slope'] == 2:
                if data['thalach'] >= 133:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['exang'] == 0.0:
        if data['trestbps'] >= 152.0:
            if data['trestbps'] >= 172.0:
                count_yes+=1
            else:
                if data['chol'] >= 298.0:
                    count_yes+=1
                else:
                    if data['chol'] >= 223.0:
                        count_no+=1
                    else:
                        if data['oldpeak'] >= 1.0:
                            count_no+=1
                        else:
                            count_yes+=1
        else:
            if data['age'] >= 59.0:
                if data['trestbps'] >= 112.0:
                    if data['oldpeak'] >= 0.4:
                        if data['oldpeak'] >= 2.0:
                            if data['chol'] >= 226.0:
                                if data['age'] >= 69.0:
                                    count_no+=1
                                else:
                                    if data['age'] >= 63.0:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                            else:
                                count_no+=1
                        else:
                            if data['oldpeak'] >= 1.1:
                                count_yes+=1
                            else:
                                if data['oldpeak'] >= 1.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                    else:
                        if data['trestbps'] >= 130.0:
                            count_no+=1
                        else:
                            count_yes+=1
                else:
                    count_no+=1
            else:
                if data['oldpeak'] >= 2.0:
                    count_no+=1
                else:
                    if data['slope'] == 0.0:
                        if data['oldpeak'] >= 1.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['oldpeak'] >= 0.4:
                            if data['age'] >= 51.0:
                                if data['oldpeak'] >= 0.5:
                                    count_yes+=1
                                else:
                                    if data['age'] >= 58.0:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                            else:
                                if data['age'] >= 46.0:
                                    if data['chol'] >= 266.0:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    count_yes+=1
                        else:
                            count_yes+=1
    else:
        if data['oldpeak'] >= 1.6:
            count_no+=1
        else:
            if data['trestbps'] >= 126.0:
                if data['chol'] >= 246.0:
                    if data['chol'] >= 261.0:
                        if data['chol'] >= 270.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['chol'] >= 207.0:
                        if data['age'] >= 66.0:
                            count_no+=1
                        else:
                            if data['oldpeak'] >= 0.2:
                                if data['oldpeak'] >= 1.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                    else:
                        if data['oldpeak'] >= 1.4:
                            count_yes+=1
                        else:
                            count_no+=1
            else:
                if data['oldpeak'] >= 0.2:
                    count_yes+=1
                else:
                    if data['age'] >= 54.0:
                        count_no+=1
                    else:
                        count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thalach'] >= 140.0:
        if data['ca'] == 0.0:
            if data['chol'] >= 274.0:
                if data['chol'] >= 321.0:
                    if data['oldpeak'] >= 0.2:
                        count_yes+=1
                    else:
                        if data['chol'] >= 330.0:
                            if data['chol'] >= 340.0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                else:
                    if data['thalach'] >= 178.0:
                        count_yes+=1
                    else:
                        if data['oldpeak'] >= 0.5:
                            count_no+=1
                        else:
                            if data['oldpeak'] >= 0.4:
                                count_yes+=1
                            else:
                                count_no+=1
            else:
                if data['chol'] >= 177.0:
                    if data['oldpeak'] >= 1.0:
                        if data['oldpeak'] >= 1.1:
                            if data['thalach'] >= 182.0:
                                if data['oldpeak'] >= 3.8:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['chol'] >= 169.0:
                        count_no+=1
                    else:
                        count_yes+=1
        else:
            if data['oldpeak'] >= 1.0:
                if data['oldpeak'] >= 1.9:
                    count_no+=1
                else:
                    if data['oldpeak'] >= 1.5:
                        count_yes+=1
                    else:
                        count_no+=1
            else:
                if data['thalach'] >= 160.0:
                    if data['sex'] == 0.0:
                        count_yes+=1
                    else:
                        if data['ca'] == 4.0:
                            count_yes+=1
                        else:
                            if data['fbs'] == 0.0:
                                count_no+=1
                            else:
                                count_yes+=1
                else:
                    if data['oldpeak'] >= 0.3:
                        if data['chol'] >= 229.0:
                            if data['chol'] >= 242.0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['chol'] >= 234.0:
                            if data['thalach'] >= 159.0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
    else:
        if data['ca'] == 0.0:
            if data['chol'] >= 237.0:
                if data['thalach'] >= 133.0:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                if data['oldpeak'] >= 1.6:
                    if data['chol'] >= 226.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['oldpeak'] >= 1.1:
                        count_yes+=1
                    else:
                        if data['oldpeak'] >= 0.9:
                            count_no+=1
                        else:
                            count_yes+=1
        else:
            if data['oldpeak'] >= 0.6:
                count_no+=1
            else:
                count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['oldpeak'] >= 1.0:
        if data['sex'] == 0.0:
            if data['exang'] == 0.0:
                if data['oldpeak'] >= 2.6:
                    count_no+=1
                else:
                    count_yes+=1
            else:
                if data['thalach'] >= 160.0:
                    count_yes+=1
                else:
                    count_no+=1
        else:
            if data['thalach'] >= 144.0:
                if data['ca'] == 0.0:
                    if data['restecg'] == 1.0:
                        if data['slope'] == 2.0:
                            if data['oldpeak'] >= 1.6:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['thalach'] >= 155.0:
                            if data['thalach'] >= 168.0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            if data['oldpeak'] >= 1.8:
                                count_yes+=1
                            else:
                                count_no+=1
                else:
                    if data['ca'] == 3.0:
                        count_yes+=1
                    else:
                        count_no+=1
            else:
                if data['oldpeak'] >= 1.2:
                    count_no+=1
                else:
                    if data['thalach'] >= 137.0:
                        count_yes+=1
                    else:
                        count_no+=1
    else:
        if data['restecg'] == 0.0:
            if data['oldpeak'] >= 0.5:
                if data['ca'] == 2.0:
                    count_no+=1
                else:
                    if data['exang'] == 0.0:
                        count_yes+=1
                    else:
                        count_no+=1
            else:
                if data['thalach'] >= 172.0:
                    if data['ca'] == 1.0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['thalach'] >= 164.0:
                        count_no+=1
                    else:
                        if data['thalach'] >= 160.0:
                            count_yes+=1
                        else:
                            if data['oldpeak'] >= 0.1:
                                if data['thalach'] >= 143.0:
                                    if data['ca'] == 0.0:
                                        if data['oldpeak'] >= 0.4:
                                            count_yes+=1
                                        else:
                                            count_no+=1
                                    else:
                                        count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                if data['thalach'] >= 125.0:
                                    count_no+=1
                                else:
                                    if data['ca'] == 0.0:
                                        count_yes+=1
                                    else:
                                        count_no+=1
        else:
            if data['ca'] == 0.0:
                if data['exang'] == 1.0:
                    if data['sex'] == 0.0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_yes+=1
            else:
                if data['oldpeak'] >= 0.6:
                    count_no+=1
                else:
                    if data['thalach'] >= 162.0:
                        if data['sex'] == 0.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['cp'] == 0.0:
        if data['oldpeak'] >= 0.8:
            if data['trestbps'] >= 118.0:
                if data['exang'] == 0.0:
                    if data['slope'] == 2.0:
                        if data['trestbps'] >= 138.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['oldpeak'] >= 2.0:
                            if data['trestbps'] >= 144.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                else:
                    count_no+=1
            else:
                if data['trestbps'] >= 112.0:
                    count_yes+=1
                else:
                    count_no+=1
        else:
            if data['ca'] == 0.0:
                if data['slope'] == 1.0:
                    if data['trestbps'] >= 135.0:
                        if data['trestbps'] >= 140.0:
                            if data['oldpeak'] >= 0.4:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['trestbps'] >= 124.0:
                            count_no+=1
                        else:
                            count_yes+=1
                else:
                    if data['trestbps'] >= 120.0:
                        count_yes+=1
                    else:
                        count_yes+=1
            else:
                if data['fbs'] == 0.0:
                    if data['trestbps'] >= 128.0:
                        if data['trestbps'] >= 140.0:
                            count_no+=1
                        else:
                            if data['exang'] == 0.0:
                                count_yes+=1
                            else:
                                count_no+=1
                    else:
                        count_no+=1
                else:
                    if data['trestbps'] >= 125.0:
                        count_no+=1
                    else:
                        count_yes+=1
    else:
        if data['slope'] == 1.0:
            if data['ca'] == 1.0:
                if data['oldpeak'] >= 0.6:
                    count_no+=1
                else:
                    count_yes+=1
            else:
                if data['trestbps'] >= 160.0:
                    if data['exang'] == 0.0:
                        if data['oldpeak'] >= 0.6:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_no+=1
                else:
                    if data['ca'] == 3.0:
                        if data['oldpeak'] >= 2.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['exang'] == 1.0:
                            if data['oldpeak'] >= 1.8:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            if data['cp'] == 1.0:
                                if data['oldpeak'] >= 1.8:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_yes+=1
        else:
            if data['cp'] == 1.0:
                if data['ca'] == 2.0:
                    if data['trestbps'] >= 160.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['oldpeak'] >= 0.3:
                        if data['oldpeak'] >= 0.7:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['trestbps'] >= 140.0:
                    if data['trestbps'] >= 142.0:
                        count_yes+=1
                    else:
                        if data['fbs'] == 0.0:
                            if data['oldpeak'] >= 1.4:
                                count_yes+=1
                            else:
                                count_yes+=1
                        else:
                            count_yes+=1
                else:
                    count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thalach'] >= 151.0:
        if data['ca'] == 2.0:
            if data['thal'] == 2.0:
                if data['fbs'] == 0.0:
                    if data['oldpeak'] >= 3.6:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_no+=1
            else:
                count_no+=1
        else:
            if data['oldpeak'] >= 3.0:
                count_no+=1
            else:
                if data['thalach'] >= 195.0:
                    if data['thal'] == 2.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['oldpeak'] >= 1.4:
                        if data['thalach'] >= 158.0:
                            if data['thal'] == 3.0:
                                if data['thalach'] >= 173.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                if data['oldpeak'] >= 1.8:
                                    if data['thalach'] >= 162.0:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['ca'] == 0.0:
                            count_yes+=1
                        else:
                            if data['sex'] == 0.0:
                                count_yes+=1
                            else:
                                if data['thalach'] >= 153.0:
                                    if data['thal'] == 2.0:
                                        count_no+=1
                                    else:
                                        if data['thalach'] >= 162.0:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                                else:
                                    count_yes+=1
    else:
        if data['ca'] == 0.0:
            if data['thal'] == 3.0:
                if data['oldpeak'] >= 0.8:
                    count_no+=1
                else:
                    if data['thalach'] >= 141.0:
                        count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['oldpeak'] >= 0.1:
                    if data['thalach'] >= 116.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['thal'] == 2.0:
                        if data['fbs'] == 0.0:
                            if data['thalach'] >= 143.0:
                                if data['sex'] == 0.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_yes+=1
        else:
            if data['oldpeak'] >= 0.6:
                if data['thalach'] >= 146.0:
                    if data['oldpeak'] >= 2.0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_no+=1
            else:
                if data['oldpeak'] >= 0.1:
                    if data['thal'] == 2.0:
                        if data['thalach'] >= 132.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_yes+=1
                else:
                    count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['exang'] == 1:
        if data['trestbps'] >= 108:
            if data['chol'] >= 354:
                if data['ca'] == 0:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                if data['chol'] >= 205:
                    if data['age'] >= 51:
                        count_no+=1
                    else:
                        if data['age'] >= 46:
                            if data['ca'] == 0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_no+=1
                else:
                    if data['chol'] >= 199:
                        count_yes+=1
                    else:
                        count_no+=1
        else:
            count_yes+=1
    else:
        if data['ca'] == 0:
            if data['sex'] == 0:
                count_yes+=1
            else:
                if data['age'] >= 67:
                    count_no+=1
                else:
                    if data['chol'] >= 243:
                        if data['chol'] >= 253:
                            if data['trestbps'] >= 124:
                                if data['restecg'] == 0:
                                    count_no+=1
                                else:
                                    if data['age'] >= 64:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                            else:
                                count_yes+=1
                        else:
                            if data['trestbps'] >= 130:
                                count_yes+=1
                            else:
                                count_no+=1
                    else:
                        if data['age'] >= 41:
                            if data['trestbps'] >= 140:
                                if data['chol'] >= 199:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                        else:
                            if data['age'] >= 39:
                                count_no+=1
                            else:
                                count_yes+=1
        else:
            if data['age'] >= 66:
                if data['ca'] == 3:
                    count_no+=1
                else:
                    count_yes+=1
            else:
                if data['ca'] == 4:
                    count_yes+=1
                else:
                    if data['age'] >= 58:
                        if data['trestbps'] >= 134:
                            count_no+=1
                        else:
                            if data['chol'] >= 303:
                                count_yes+=1
                            else:
                                count_no+=1
                    else:
                        if data['fbs'] == 0:
                            if data['chol'] >= 303:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['oldpeak'] >= 0.8:
        if data['cp'] == 0.0:
            if data['thalach'] >= 181.0:
                count_yes+=1
            else:
                if data['trestbps'] >= 110.0:
                    if data['thal'] == 3.0:
                        count_no+=1
                    else:
                        if data['thalach'] >= 160.0:
                            count_yes+=1
                        else:
                            if data['ca'] == 0.0:
                                if data['oldpeak'] >= 2.3:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_no+=1
                else:
                    if data['thalach'] >= 125.0:
                        count_no+=1
                    else:
                        count_yes+=1
        else:
            if data['sex'] == 0.0:
                count_yes+=1
            else:
                if data['ca'] == 0.0:
                    if data['cp'] == 1.0:
                        if data['thalach'] >= 178.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['thalach'] >= 137.0:
                            count_yes+=1
                        else:
                            count_no+=1
                else:
                    if data['thalach'] >= 146.0:
                        if data['ca'] == 2.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
    else:
        if data['trestbps'] >= 148.0:
            if data['trestbps'] >= 150.0:
                if data['thalach'] >= 195.0:
                    count_no+=1
                else:
                    if data['thalach'] >= 154.0:
                        if data['cp'] == 3.0:
                            if data['thalach'] >= 159.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_yes+=1
                    else:
                        if data['exang'] == 0.0:
                            count_yes+=1
                        else:
                            count_no+=1
            else:
                count_no+=1
        else:
            if data['exang'] == 0.0:
                if data['ca'] == 2.0:
                    if data['thalach'] >= 179.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['thal'] == 3.0:
                        if data['trestbps'] >= 124.0:
                            if data['trestbps'] >= 130.0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['trestbps'] >= 140.0:
                            if data['thalach'] >= 158.0:
                                if data['thalach'] >= 180.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_yes+=1
            else:
                if data['thalach'] >= 154.0:
                    count_yes+=1
                else:
                    count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thalach'] >= 151:
        if data['age'] >= 58:
            if data['cp'] == 2:
                if data['age'] >= 59:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                if data['thalach'] >= 179:
                    count_yes+=1
                else:
                    if data['chol'] >= 325:
                        count_yes+=1
                    else:
                        if data['chol'] >= 244:
                            if data['thalach'] >= 152:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            if data['chol'] >= 209:
                                count_yes+=1
                            else:
                                count_no+=1
        else:
            if data['cp'] == 0:
                if data['trestbps'] >= 115:
                    if data['trestbps'] >= 124:
                        if data['age'] >= 54:
                            count_yes+=1
                        else:
                            if data['thalach'] >= 178:
                                if data['age'] >= 42:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['sex'] == 0:
                        count_yes+=1
                    else:
                        count_no+=1
            else:
                if data['age'] >= 57:
                    count_no+=1
                else:
                    if data['trestbps'] >= 140:
                        if data['sex'] == 0:
                            count_yes+=1
                        else:
                            if data['age'] >= 50:
                                count_no+=1
                            else:
                                count_yes+=1
                    else:
                        count_yes+=1
    else:
        if data['cp'] == 0:
            if data['trestbps'] >= 120:
                if data['age'] >= 66:
                    if data['age'] >= 67:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['chol'] >= 198:
                        count_no+=1
                    else:
                        if data['chol'] >= 197:
                            count_yes+=1
                        else:
                            count_no+=1
            else:
                if data['chol'] >= 206:
                    count_no+=1
                else:
                    count_yes+=1
        else:
            if data['sex'] == 0:
                if data['thalach'] >= 114:
                    count_yes+=1
                else:
                    if data['age'] >= 62:
                        count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['cp'] == 1:
                    count_yes+=1
                else:
                    if data['chol'] >= 222:
                        if data['trestbps'] >= 128:
                            if data['fbs'] == 0:
                                count_no+=1
                            else:
                                if data['age'] >= 68:
                                    count_no+=1
                                else:
                                    count_yes+=1
                        else:
                            if data['age'] >= 51:
                                count_yes+=1
                            else:
                                count_no+=1
                    else:
                        count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thalach'] >= 148.0:
        if data['trestbps'] >= 140.0:
            if data['oldpeak'] >= 0.8:
                if data['oldpeak'] >= 1.6:
                    if data['trestbps'] >= 150.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    count_no+=1
            else:
                if data['thalach'] >= 159.0:
                    if data['thal'] == 2.0:
                        count_yes+=1
                    else:
                        if data['fbs'] == 0.0:
                            count_no+=1
                        else:
                            count_yes+=1
                else:
                    count_yes+=1
        else:
            if data['sex'] == 0.0:
                if data['oldpeak'] >= 1.8:
                    count_no+=1
                else:
                    if data['fbs'] == 0.0:
                        if data['restecg'] == 0.0:
                            if data['thalach'] >= 169.0:
                                if data['thalach'] >= 172.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_yes+=1
                    else:
                        if data['restecg'] == 0.0:
                            count_no+=1
                        else:
                            count_yes+=1
            else:
                if data['trestbps'] >= 108.0:
                    if data['trestbps'] >= 118.0:
                        if data['trestbps'] >= 124.0:
                            if data['thal'] == 2.0:
                                if data['trestbps'] >= 128.0:
                                    if data['oldpeak'] >= 1.4:
                                        if data['restecg'] == 0.0:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                                    else:
                                        count_yes+=1
                                else:
                                    if data['thalach'] >= 162.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                            else:
                                if data['trestbps'] >= 130.0:
                                    if data['thalach'] >= 163.0:
                                        if data['thalach'] >= 173.0:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    count_no+=1
                        else:
                            if data['oldpeak'] >= 3.8:
                                count_no+=1
                            else:
                                if data['thalach'] >= 162.0:
                                    count_yes+=1
                                else:
                                    if data['restecg'] == 0.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                    else:
                        if data['thalach'] >= 165.0:
                            if data['thalach'] >= 179.0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            if data['thalach'] >= 161.0:
                                count_yes+=1
                            else:
                                if data['thalach'] >= 153.0:
                                    if data['thalach'] >= 160.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_no+=1
                else:
                    count_yes+=1
    else:
        if data['oldpeak'] >= 0.8:
            if data['thal'] == 3.0:
                if data['thalach'] >= 146.0:
                    if data['restecg'] == 0.0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_no+=1
            else:
                if data['thalach'] >= 122.0:
                    if data['oldpeak'] >= 2.8:
                        count_no+=1
                    else:
                        if data['trestbps'] >= 110.0:
                            if data['fbs'] == 0.0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_no+=1
                else:
                    count_no+=1
        else:
            if data['sex'] == 0.0:
                count_yes+=1
            else:
                if data['trestbps'] >= 120.0:
                    count_yes+=1
                else:
                    if data['restecg'] == 0.0:
                        count_no+=1
                    else:
                        count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['exang'] == 0:
        if data['age'] >= 58:
            if data['sex'] == 0:
                if data['ca'] == 3:
                    count_no+=1
                else:
                    if data['age'] >= 64:
                        count_yes+=1
                    else:
                        if data['ca'] == 0:
                            count_yes+=1
                        else:
                            count_no+=1
            else:
                if data['ca'] == 0:
                    if data['chol'] >= 237:
                        if data['restecg'] == 0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['trestbps'] >= 160:
                        count_yes+=1
                    else:
                        if data['ca'] == 3:
                            if data['chol'] >= 322:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
        else:
            if data['trestbps'] >= 115:
                if data['chol'] >= 192:
                    if data['ca'] == 2:
                        if data['chol'] >= 244:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['age'] >= 57:
                            if data['chol'] >= 236:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            if data['age'] >= 41:
                                count_yes+=1
                            else:
                                if data['chol'] >= 223:
                                    count_no+=1
                                else:
                                    count_yes+=1
                else:
                    if data['chol'] >= 188:
                        count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['sex'] == 0:
                    count_yes+=1
                else:
                    count_no+=1
    else:
        if data['sex'] == 1:
            if data['chol'] >= 267:
                count_no+=1
            else:
                if data['chol'] >= 261:
                    count_yes+=1
                else:
                    if data['trestbps'] >= 142:
                        count_yes+=1
                    else:
                        if data['trestbps'] >= 110:
                            if data['chol'] >= 212:
                                count_no+=1
                            else:
                                if data['chol'] >= 207:
                                    count_yes+=1
                                else:
                                    count_no+=1
                        else:
                            count_yes+=1
        else:
            if data['age'] >= 55:
                if data['chol'] >= 354:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                if data['chol'] >= 305:
                    count_no+=1
                else:
                    count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['oldpeak'] >= 1.8:
        if data['slope'] == 2.0:
            if data['exang'] == 0.0:
                count_yes+=1
            else:
                count_no+=1
        else:
            if data['chol'] >= 258.0:
                count_no+=1
            else:
                if data['chol'] >= 245.0:
                    count_yes+=1
                else:
                    if data['oldpeak'] >= 2.0:
                        if data['age'] >= 46.0:
                            count_no+=1
                        else:
                            if data['chol'] >= 208.0:
                                count_yes+=1
                            else:
                                count_no+=1
                    else:
                        count_yes+=1
    else:
        if data['exang'] == 1.0:
            if data['chol'] >= 241.0:
                if data['age'] >= 43.0:
                    if data['age'] >= 74.0:
                        if data['chol'] >= 304.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['chol'] >= 288.0:
                            if data['chol'] >= 289.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                else:
                    count_yes+=1
            else:
                if data['age'] >= 60.0:
                    count_no+=1
                else:
                    if data['chol'] >= 221.0:
                        count_yes+=1
                    else:
                        if data['oldpeak'] >= 1.4:
                            count_yes+=1
                        else:
                            count_no+=1
        else:
            if data['chol'] >= 221.0:
                if data['age'] >= 57.0:
                    if data['chol'] >= 265.0:
                        count_yes+=1
                    else:
                        if data['age'] >= 69.0:
                            count_yes+=1
                        else:
                            if data['chol'] >= 229.0:
                                if data['chol'] >= 248.0:
                                    if data['age'] >= 62.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                else:
                    count_yes+=1
            else:
                if data['chol'] >= 212.0:
                    if data['slope'] == 2.0:
                        count_yes+=1
                    else:
                        if data['oldpeak'] >= 1.6:
                            count_yes+=1
                        else:
                            count_no+=1
                else:
                    if data['age'] >= 41.0:
                        if data['age'] >= 45.0:
                            if data['oldpeak'] >= 0.8:
                                if data['oldpeak'] >= 1.5:
                                    count_yes+=1
                                else:
                                    if data['chol'] >= 197.0:
                                        if data['chol'] >= 204.0:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                                    else:
                                        count_no+=1
                            else:
                                if data['age'] >= 61.0:
                                    if data['chol'] >= 203.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_yes+=1
                        else:
                            if data['chol'] >= 203.0:
                                count_yes+=1
                            else:
                                if data['chol'] >= 180.0:
                                    if data['chol'] >= 197.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_no+=1
                    else:
                        count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thal'] == 3.0:
        if data['oldpeak'] >= 0.8:
            if data['thalach'] >= 194.0:
                count_yes+=1
            else:
                if data['thalach'] >= 151.0:
                    if data['oldpeak'] >= 2.5:
                        count_no+=1
                    else:
                        if data['thalach'] >= 168.0:
                            if data['thalach'] >= 178.0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                else:
                    count_no+=1
        else:
            if data['slope'] == 1.0:
                if data['thalach'] >= 163.0:
                    count_no+=1
                else:
                    if data['ca'] == 3.0:
                        count_no+=1
                    else:
                        if data['ca'] == 1.0:
                            if data['thalach'] >= 150.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_yes+=1
            else:
                if data['fbs'] == 0.0:
                    if data['thalach'] >= 141.0:
                        if data['oldpeak'] >= 0.1:
                            count_no+=1
                        else:
                            if data['thalach'] >= 162.0:
                                count_no+=1
                            else:
                                count_yes+=1
                    else:
                        count_yes+=1
                else:
                    count_yes+=1
    else:
        if data['oldpeak'] >= 1.2:
            if data['thalach'] >= 115.0:
                if data['ca'] == 1.0:
                    if data['thalach'] >= 144.0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['oldpeak'] >= 3.4:
                        count_no+=1
                    else:
                        if data['thalach'] >= 160.0:
                            if data['thalach'] >= 161.0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            if data['thal'] == 2.0:
                                count_yes+=1
                            else:
                                if data['ca'] == 0.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
            else:
                count_no+=1
        else:
            if data['thalach'] >= 137.0:
                if data['thal'] == 0.0:
                    count_no+=1
                else:
                    if data['ca'] == 0.0:
                        if data['thalach'] >= 170.0:
                            count_yes+=1
                        else:
                            if data['thalach'] >= 169.0:
                                if data['slope'] == 2.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_yes+=1
                    else:
                        if data['thalach'] >= 168.0:
                            count_yes+=1
                        else:
                            if data['thalach'] >= 164.0:
                                count_no+=1
                            else:
                                if data['ca'] == 1.0:
                                    count_yes+=1
                                else:
                                    if data['thalach'] >= 162.0:
                                        if data['oldpeak'] >= 0.8:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                                    else:
                                        count_no+=1
            else:
                if data['thalach'] >= 136.0:
                    count_no+=1
                else:
                    if data['thalach'] >= 125.0:
                        if data['thalach'] >= 130.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thal'] == 2:
        if data['exang'] == 1:
            if data['cp'] == 0:
                if data['chol'] >= 354:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                count_yes+=1
        else:
            if data['chol'] >= 330:
                if data['chol'] >= 342:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                if data['sex'] == 0:
                    if data['cp'] == 1:
                        if data['slope'] == 1:
                            if data['chol'] >= 250:
                                count_yes+=1
                            else:
                                if data['chol'] >= 236:
                                    count_no+=1
                                else:
                                    count_yes+=1
                        else:
                            count_yes+=1
                    else:
                        count_yes+=1
                else:
                    if data['slope'] == 1:
                        if data['chol'] >= 302:
                            count_yes+=1
                        else:
                            if data['cp'] == 2:
                                if data['chol'] >= 214:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_no+=1
                    else:
                        if data['chol'] >= 232:
                            if data['chol'] >= 235:
                                if data['cp'] == 0:
                                    if data['chol'] >= 290:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    if data['chol'] >= 246:
                                        count_yes+=1
                                    else:
                                        if data['chol'] >= 243:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
    else:
        if data['cp'] == 0:
            if data['slope'] == 2:
                if data['chol'] >= 253:
                    count_no+=1
                else:
                    if data['chol'] >= 226:
                        count_yes+=1
                    else:
                        if data['chol'] >= 223:
                            count_no+=1
                        else:
                            if data['chol'] >= 207:
                                count_yes+=1
                            else:
                                count_no+=1
            else:
                if data['thal'] == 1:
                    if data['slope'] == 0:
                        count_no+=1
                    else:
                        if data['sex'] == 0:
                            count_no+=1
                        else:
                            count_yes+=1
                else:
                    if data['chol'] >= 234:
                        if data['chol'] >= 241:
                            if data['chol'] >= 266:
                                count_no+=1
                            else:
                                if data['chol'] >= 263:
                                    count_yes+=1
                                else:
                                    count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
        else:
            if data['chol'] >= 212:
                if data['chol'] >= 298:
                    if data['exang'] == 0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['slope'] == 0:
                        count_yes+=1
                    else:
                        if data['chol'] >= 224:
                            if data['chol'] >= 231:
                                if data['chol'] >= 256:
                                    if data['chol'] >= 261:
                                        count_no+=1
                                    else:
                                        if data['exang'] == 0:
                                            count_yes+=1
                                        else:
                                            count_no+=1
                                else:
                                    if data['exang'] == 0:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                            else:
                                count_no+=1
                        else:
                            if data['cp'] == 1:
                                count_yes+=1
                            else:
                                count_no+=1
            else:
                if data['cp'] == 2:
                    if data['slope'] == 1:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['exang'] == 1.0:
        if data['oldpeak'] >= 0.9:
            if data['slope'] == 0.0:
                if data['thalach'] >= 160.0:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                if data['oldpeak'] >= 1.2:
                    count_no+=1
                else:
                    if data['chol'] >= 243.0:
                        if data['chol'] >= 275.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
        else:
            if data['thalach'] >= 163.0:
                count_yes+=1
            else:
                if data['thalach'] >= 120.0:
                    if data['trestbps'] >= 124.0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_yes+=1
    else:
        if data['oldpeak'] >= 1.9:
            if data['trestbps'] >= 132.0:
                if data['thalach'] >= 128.0:
                    count_no+=1
                else:
                    if data['trestbps'] >= 150.0:
                        count_yes+=1
                    else:
                        count_no+=1
            else:
                if data['chol'] >= 245.0:
                    count_yes+=1
                else:
                    count_no+=1
        else:
            if data['sex'] == 0.0:
                if data['chol'] >= 319.0:
                    if data['chol'] >= 342.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['thalach'] >= 115.0:
                        if data['thalach'] >= 174.0:
                            if data['chol'] >= 236.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
            else:
                if data['trestbps'] >= 128.0:
                    if data['chol'] >= 273.0:
                        if data['chol'] >= 308.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['chol'] >= 212.0:
                            if data['trestbps'] >= 130.0:
                                if data['thalach'] >= 181.0:
                                    if data['chol'] >= 271.0:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    if data['chol'] >= 254.0:
                                        if data['chol'] >= 266.0:
                                            count_yes+=1
                                        else:
                                            count_no+=1
                                    else:
                                        if data['trestbps'] >= 152.0:
                                            if data['trestbps'] >= 156.0:
                                                count_yes+=1
                                            else:
                                                count_no+=1
                                        else:
                                            count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                else:
                    if data['trestbps'] >= 124.0:
                        count_no+=1
                    else:
                        if data['chol'] >= 175.0:
                            if data['thalach'] >= 123.0:
                                if data['oldpeak'] >= 0.4:
                                    count_yes+=1
                                else:
                                    if data['thalach'] >= 156.0:
                                        if data['chol'] >= 260.0:
                                            count_yes+=1
                                        else:
                                            if data['chol'] >= 230.0:
                                                count_no+=1
                                            else:
                                                count_yes+=1
                                    else:
                                        count_no+=1
                            else:
                                count_no+=1
                        else:
                            count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thal'] == 2:
        if data['thalach'] >= 138:
            if data['age'] >= 57:
                if data['slope'] == 2:
                    if data['age'] >= 59:
                        if data['age'] >= 77:
                            count_no+=1
                        else:
                            if data['thalach'] >= 158:
                                if data['age'] >= 64:
                                    count_no+=1
                                else:
                                    if data['thalach'] >= 169:
                                        if data['trestbps'] >= 135:
                                            count_yes+=1
                                        else:
                                            count_no+=1
                                    else:
                                        count_yes+=1
                            else:
                                count_yes+=1
                    else:
                        if data['trestbps'] >= 136:
                            count_no+=1
                        else:
                            count_yes+=1
                else:
                    if data['trestbps'] >= 146:
                        count_yes+=1
                    else:
                        count_no+=1
            else:
                if data['trestbps'] >= 112:
                    if data['thalach'] >= 149:
                        count_yes+=1
                    else:
                        if data['thalach'] >= 144:
                            count_no+=1
                        else:
                            count_yes+=1
                else:
                    if data['age'] >= 45:
                        if data['trestbps'] >= 108:
                            if data['trestbps'] >= 110:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
        else:
            if data['age'] >= 66:
                if data['thalach'] >= 114:
                    if data['trestbps'] >= 110:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    count_no+=1
            else:
                if data['trestbps'] >= 110:
                    count_no+=1
                else:
                    count_yes+=1
    else:
        if data['thalach'] >= 173:
            if data['trestbps'] >= 152:
                count_no+=1
            else:
                count_yes+=1
        else:
            if data['trestbps'] >= 110:
                if data['exang'] == 0:
                    if data['thalach'] >= 163:
                        if data['trestbps'] >= 150:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['thalach'] >= 145:
                            if data['age'] >= 67:
                                if data['trestbps'] >= 140:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                if data['age'] >= 43:
                                    if data['trestbps'] >= 150:
                                        if data['trestbps'] >= 170:
                                            count_yes+=1
                                        else:
                                            count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_no+=1
                        else:
                            if data['slope'] == 2:
                                count_yes+=1
                            else:
                                count_no+=1
                else:
                    if data['age'] >= 64:
                        if data['thalach'] >= 131:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
            else:
                count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['ca'] == 0:
        if data['cp'] == 0:
            if data['chol'] >= 197:
                if data['age'] >= 42:
                    if data['age'] >= 50:
                        if data['chol'] >= 394:
                            count_yes+=1
                        else:
                            if data['chol'] >= 237:
                                if data['chol'] >= 241:
                                    count_no+=1
                                else:
                                    if data['age'] >= 67:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                            else:
                                if data['chol'] >= 207:
                                    count_yes+=1
                                else:
                                    if data['age'] >= 63:
                                        count_no+=1
                                    else:
                                        if data['restecg'] == 0:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                    else:
                        if data['age'] >= 46:
                            if data['age'] >= 48:
                                count_yes+=1
                            else:
                                if data['slope'] == 1:
                                    count_yes+=1
                                else:
                                    count_no+=1
                        else:
                            count_yes+=1
                else:
                    count_no+=1
            else:
                count_yes+=1
        else:
            if data['age'] >= 67:
                if data['age'] >= 68:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                if data['chol'] >= 261:
                    if data['cp'] == 3:
                        count_no+=1
                    else:
                        if data['chol'] >= 268:
                            count_yes+=1
                        else:
                            count_no+=1
                else:
                    count_yes+=1
    else:
        if data['age'] >= 45:
            if data['age'] >= 68:
                if data['slope'] == 1:
                    count_no+=1
                else:
                    count_yes+=1
            else:
                if data['chol'] >= 303:
                    if data['age'] >= 57:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['age'] >= 55:
                        count_no+=1
                    else:
                        if data['slope'] == 0:
                            count_yes+=1
                        else:
                            if data['cp'] == 3:
                                count_yes+=1
                            else:
                                if data['chol'] >= 206:
                                    count_no+=1
                                else:
                                    if data['slope'] == 1:
                                        count_no+=1
                                    else:
                                        count_yes+=1
        else:
            count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['oldpeak'] >= 0.8:
        if data['slope'] == 1.0:
            if data['chol'] >= 218.0:
                if data['sex'] == 1.0:
                    if data['chol'] >= 234.0:
                        count_no+=1
                    else:
                        if data['chol'] >= 231.0:
                            if data['oldpeak'] >= 3.6:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                else:
                    if data['trestbps'] >= 150.0:
                        count_no+=1
                    else:
                        if data['oldpeak'] >= 1.9:
                            count_no+=1
                        else:
                            count_yes+=1
            else:
                if data['chol'] >= 214.0:
                    count_yes+=1
                else:
                    if data['trestbps'] >= 120.0:
                        if data['chol'] >= 198.0:
                            count_no+=1
                        else:
                            if data['chol'] >= 193.0:
                                count_yes+=1
                            else:
                                count_no+=1
                    else:
                        count_yes+=1
        else:
            if data['oldpeak'] >= 2.2:
                if data['restecg'] == 0.0:
                    count_no+=1
                else:
                    if data['chol'] >= 226.0:
                        count_yes+=1
                    else:
                        count_no+=1
            else:
                if data['trestbps'] >= 118.0:
                    if data['chol'] >= 168.0:
                        if data['trestbps'] >= 150.0:
                            if data['sex'] == 0.0:
                                count_yes+=1
                            else:
                                if data['restecg'] == 0.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
                else:
                    count_no+=1
    else:
        if data['chol'] >= 175.0:
            if data['chol'] >= 230.0:
                if data['chol'] >= 233.0:
                    if data['sex'] == 1.0:
                        if data['chol'] >= 276.0:
                            count_no+=1
                        else:
                            if data['trestbps'] >= 112.0:
                                if data['oldpeak'] >= 0.6:
                                    count_no+=1
                                else:
                                    if data['chol'] >= 256.0:
                                        if data['chol'] >= 257.0:
                                            if data['slope'] == 1.0:
                                                count_yes+=1
                                            else:
                                                if data['oldpeak'] >= 0.3:
                                                    count_no+=1
                                                else:
                                                    count_yes+=1
                                        else:
                                            count_no+=1
                                    else:
                                        count_yes+=1
                            else:
                                if data['slope'] == 1.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                    else:
                        if data['chol'] >= 330.0:
                            if data['restecg'] == 0.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_yes+=1
                else:
                    count_no+=1
            else:
                if data['chol'] >= 178.0:
                    count_yes+=1
                else:
                    if data['oldpeak'] >= 0.4:
                        count_yes+=1
                    else:
                        count_no+=1
        else:
            if data['restecg'] == 0.0:
                count_no+=1
            else:
                count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['oldpeak'] >= 1.9:
        if data['thalach'] >= 187.0:
            count_yes+=1
        else:
            if data['thalach'] >= 150.0:
                if data['oldpeak'] >= 2.6:
                    count_no+=1
                else:
                    count_yes+=1
            else:
                if data['trestbps'] >= 178.0:
                    count_yes+=1
                else:
                    if data['slope'] == 2.0:
                        if data['trestbps'] >= 160.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['age'] >= 66.0:
                            if data['age'] >= 67.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
    else:
        if data['age'] >= 58.0:
            if data['thalach'] >= 158.0:
                if data['oldpeak'] >= 0.2:
                    if data['age'] >= 67.0:
                        if data['thalach'] >= 163.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['thalach'] >= 169.0:
                        count_no+=1
                    else:
                        if data['thalach'] >= 160.0:
                            count_yes+=1
                        else:
                            count_no+=1
            else:
                if data['age'] >= 68.0:
                    count_yes+=1
                else:
                    if data['thalach'] >= 140.0:
                        if data['age'] >= 62.0:
                            if data['thalach'] >= 147.0:
                                if data['thalach'] >= 151.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                        else:
                            if data['thalach'] >= 154.0:
                                count_yes+=1
                            else:
                                count_no+=1
                    else:
                        if data['thalach'] >= 111.0:
                            if data['age'] >= 59.0:
                                count_no+=1
                            else:
                                if data['thalach'] >= 131.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                        else:
                            if data['thalach'] >= 96.0:
                                count_yes+=1
                            else:
                                count_no+=1
        else:
            if data['thalach'] >= 147.0:
                if data['trestbps'] >= 118.0:
                    if data['thalach'] >= 166.0:
                        if data['thalach'] >= 169.0:
                            if data['trestbps'] >= 152.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            if data['trestbps'] >= 132.0:
                                count_yes+=1
                            else:
                                count_no+=1
                    else:
                        if data['fbs'] == 0.0:
                            count_yes+=1
                        else:
                            if data['thalach'] >= 152.0:
                                count_yes+=1
                            else:
                                count_no+=1
                else:
                    if data['thalach'] >= 159.0:
                        if data['slope'] == 0.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
            else:
                if data['age'] >= 51.0:
                    if data['trestbps'] >= 150.0:
                        count_no+=1
                    else:
                        if data['fbs'] == 0.0:
                            if data['restecg'] == 0.0:
                                count_yes+=1
                            else:
                                if data['trestbps'] >= 124.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                        else:
                            count_no+=1
                else:
                    if data['trestbps'] >= 118.0:
                        count_no+=1
                    else:
                        count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thal'] == 2:
        if data['ca'] == 0:
            if data['chol'] >= 330:
                if data['chol'] >= 342:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                if data['restecg'] == 1:
                    if data['thalach'] >= 137:
                        if data['slope'] == 1:
                            if data['chol'] >= 244:
                                if data['chol'] >= 271:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_yes+=1
                    else:
                        if data['slope'] == 1:
                            count_no+=1
                        else:
                            count_yes+=1
                else:
                    count_yes+=1
        else:
            if data['restecg'] == 0:
                if data['fbs'] == 0:
                    if data['slope'] == 2:
                        if data['chol'] >= 213:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_no+=1
                else:
                    if data['ca'] == 1:
                        if data['thalach'] >= 174:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
            else:
                if data['chol'] >= 242:
                    count_yes+=1
                else:
                    if data['thalach'] >= 163:
                        count_yes+=1
                    else:
                        if data['thalach'] >= 160:
                            count_no+=1
                        else:
                            count_yes+=1
    else:
        if data['thalach'] >= 145:
            if data['chol'] >= 231:
                if data['ca'] == 1:
                    if data['thalach'] >= 156:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['chol'] >= 274:
                        if data['restecg'] == 0:
                            if data['chol'] >= 564:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['chol'] >= 232:
                            count_yes+=1
                        else:
                            if data['ca'] == 0:
                                count_no+=1
                            else:
                                count_yes+=1
            else:
                if data['chol'] >= 203:
                    count_no+=1
                else:
                    if data['chol'] >= 186:
                        count_yes+=1
                    else:
                        count_no+=1
        else:
            if data['slope'] == 2:
                if data['restecg'] == 0:
                    if data['chol'] >= 249:
                        count_no+=1
                    else:
                        if data['chol'] >= 226:
                            count_yes+=1
                        else:
                            count_no+=1
                else:
                    count_yes+=1
            else:
                if data['thal'] == 3:
                    count_no+=1
                else:
                    if data['restecg'] == 1:
                        if data['chol'] >= 315:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['ca'] == 0.0:
        if data['exang'] == 0.0:
            if data['cp'] == 1.0:
                if data['oldpeak'] >= 0.3:
                    if data['oldpeak'] >= 0.7:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    count_yes+=1
            else:
                if data['cp'] == 2.0:
                    count_yes+=1
                else:
                    if data['oldpeak'] >= 0.6:
                        if data['oldpeak'] >= 2.6:
                            if data['restecg'] == 0.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            if data['restecg'] == 0.0:
                                count_yes+=1
                            else:
                                if data['oldpeak'] >= 1.0:
                                    if data['oldpeak'] >= 1.2:
                                        if data['cp'] == 0.0:
                                            count_yes+=1
                                        else:
                                            if data['fbs'] == 0.0:
                                                count_no+=1
                                            else:
                                                count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    count_yes+=1
                    else:
                        if data['oldpeak'] >= 0.5:
                            count_no+=1
                        else:
                            if data['oldpeak'] >= 0.2:
                                if data['oldpeak'] >= 0.4:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                if data['restecg'] == 0.0:
                                    if data['cp'] == 0.0:
                                        count_yes+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_yes+=1
        else:
            if data['oldpeak'] >= 0.8:
                if data['cp'] == 0.0:
                    if data['oldpeak'] >= 1.5:
                        if data['oldpeak'] >= 2.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['restecg'] == 0.0:
                        count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['restecg'] == 0.0:
                    count_yes+=1
                else:
                    if data['oldpeak'] >= 0.6:
                        count_yes+=1
                    else:
                        count_yes+=1
    else:
        if data['cp'] == 0.0:
            if data['restecg'] == 1.0:
                if data['oldpeak'] >= 1.2:
                    count_no+=1
                else:
                    if data['oldpeak'] >= 0.3:
                        count_yes+=1
                    else:
                        count_no+=1
            else:
                count_no+=1
        else:
            if data['oldpeak'] >= 2.0:
                count_no+=1
            else:
                if data['cp'] == 3.0:
                    if data['restecg'] == 0.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['restecg'] == 1.0:
                        if data['oldpeak'] >= 1.2:
                            if data['oldpeak'] >= 1.9:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['cp'] == 1.0:
                            count_no+=1
                        else:
                            if data['oldpeak'] >= 0.5:
                                count_yes+=1
                            else:
                                if data['oldpeak'] >= 0.4:
                                    count_no+=1
                                else:
                                    count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thal'] == 2.0:
        if data['ca'] == 1.0:
            if data['sex'] == 1.0:
                if data['oldpeak'] >= 1.4:
                    if data['age'] >= 64.0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['restecg'] == 0.0:
                        count_no+=1
                    else:
                        if data['oldpeak'] >= 0.8:
                            count_yes+=1
                        else:
                            count_no+=1
            else:
                if data['restecg'] == 0.0:
                    if data['age'] >= 71.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    count_yes+=1
        else:
            if data['oldpeak'] >= 2.4:
                if data['oldpeak'] >= 3.6:
                    count_no+=1
                else:
                    if data['ca'] == 0.0:
                        if data['exang'] == 0.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_no+=1
            else:
                if data['age'] >= 59.0:
                    if data['sex'] == 0.0:
                        if data['exang'] == 1.0:
                            if data['age'] >= 64.0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            if data['age'] >= 62.0:
                                count_yes+=1
                            else:
                                if data['restecg'] == 0.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                    else:
                        if data['exang'] == 0.0:
                            if data['age'] >= 70.0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                else:
                    if data['oldpeak'] >= 1.8:
                        if data['age'] >= 58.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['sex'] == 0.0:
                            count_yes+=1
                        else:
                            if data['age'] >= 47.0:
                                if data['age'] >= 48.0:
                                    count_yes+=1
                                else:
                                    count_yes+=1
                            else:
                                count_yes+=1
    else:
        if data['age'] >= 65.0:
            if data['oldpeak'] >= 2.0:
                count_no+=1
            else:
                if data['exang'] == 0.0:
                    if data['restecg'] == 0.0:
                        if data['sex'] == 0.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_no+=1
        else:
            if data['oldpeak'] >= 0.1:
                if data['oldpeak'] >= 4.2:
                    if data['restecg'] == 0.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['age'] >= 43.0:
                        if data['exang'] == 0.0:
                            if data['oldpeak'] >= 1.6:
                                if data['oldpeak'] >= 2.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_no+=1
                    else:
                        if data['age'] >= 40.0:
                            if data['restecg'] == 0.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
            else:
                if data['ca'] == 2.0:
                    count_no+=1
                else:
                    if data['age'] >= 56.0:
                        count_yes+=1
                    else:
                        if data['exang'] == 1.0:
                            if data['age'] >= 52.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thal'] == 2.0:
        if data['oldpeak'] >= 2.2:
            if data['restecg'] == 1.0:
                count_yes+=1
            else:
                if data['chol'] >= 208.0:
                    if data['chol'] >= 246.0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_no+=1
        else:
            if data['restecg'] == 0.0:
                if data['exang'] == 0.0:
                    if data['chol'] >= 232.0:
                        if data['chol'] >= 234.0:
                            if data['chol'] >= 282.0:
                                if data['sex'] == 0.0:
                                    if data['chol'] >= 330.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                if data['oldpeak'] >= 0.5:
                                    count_yes+=1
                                else:
                                    if data['sex'] == 0.0:
                                        if data['chol'] >= 265.0:
                                            count_yes+=1
                                        else:
                                            if data['chol'] >= 236.0:
                                                count_no+=1
                                            else:
                                                count_yes+=1
                                    else:
                                        if data['chol'] >= 273.0:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['chol'] >= 182.0:
                            if data['chol'] >= 204.0:
                                count_yes+=1
                            else:
                                if data['chol'] >= 197.0:
                                    if data['oldpeak'] >= 1.2:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    count_yes+=1
                        else:
                            count_no+=1
                else:
                    if data['chol'] >= 211.0:
                        count_yes+=1
                    else:
                        if data['oldpeak'] >= 1.4:
                            count_yes+=1
                        else:
                            count_no+=1
            else:
                if data['oldpeak'] >= 1.8:
                    if data['chol'] >= 303.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['chol'] >= 198.0:
                        count_yes+=1
                    else:
                        if data['exang'] == 0.0:
                            count_yes+=1
                        else:
                            count_no+=1
    else:
        if data['chol'] >= 204.0:
            if data['exang'] == 1.0:
                if data['oldpeak'] >= 0.6:
                    count_no+=1
                else:
                    if data['chol'] >= 241.0:
                        if data['chol'] >= 263.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['chol'] >= 309.0:
                    if data['oldpeak'] >= 4.0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['oldpeak'] >= 2.3:
                        if data['oldpeak'] >= 2.5:
                            if data['oldpeak'] >= 4.2:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['oldpeak'] >= 0.1:
                            if data['oldpeak'] >= 0.4:
                                if data['oldpeak'] >= 1.2:
                                    if data['oldpeak'] >= 1.8:
                                        if data['oldpeak'] >= 2.0:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    if data['chol'] >= 227.0:
                                        if data['thal'] == 1.0:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                                    else:
                                        count_no+=1
                            else:
                                count_no+=1
                        else:
                            if data['chol'] >= 223.0:
                                count_no+=1
                            else:
                                count_yes+=1
        else:
            if data['oldpeak'] >= 1.6:
                count_no+=1
            else:
                if data['chol'] >= 197.0:
                    count_yes+=1
                else:
                    if data['restecg'] == 0.0:
                        count_yes+=1
                    else:
                        if data['exang'] == 0.0:
                            if data['oldpeak'] >= 1.4:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['cp'] == 0:
        if data['thal'] == 2:
            if data['age'] >= 44:
                if data['age'] >= 64:
                    if data['age'] >= 77:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['sex'] == 0:
                        if data['age'] >= 59:
                            count_no+=1
                        else:
                            if data['restecg'] == 0:
                                count_yes+=1
                            else:
                                count_no+=1
                    else:
                        count_no+=1
            else:
                count_yes+=1
        else:
            if data['restecg'] == 1:
                if data['age'] >= 59:
                    if data['age'] >= 62:
                        if data['slope'] == 1:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['slope'] == 1:
                            count_yes+=1
                        else:
                            count_no+=1
                else:
                    if data['thal'] == 1:
                        if data['age'] >= 57:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['slope'] == 1:
                            count_no+=1
                        else:
                            if data['age'] >= 51:
                                if data['age'] >= 57:
                                    if data['age'] >= 58:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
            else:
                if data['age'] >= 54:
                    count_no+=1
                else:
                    if data['age'] >= 53:
                        count_yes+=1
                    else:
                        count_no+=1
    else:
        if data['slope'] == 1:
            if data['sex'] == 1:
                if data['age'] >= 65:
                    if data['thal'] == 2:
                        if data['age'] >= 69:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_no+=1
                else:
                    if data['thal'] == 2:
                        if data['cp'] == 2:
                            if data['restecg'] == 0:
                                if data['age'] >= 60:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_yes+=1
                        else:
                            count_yes+=1
                    else:
                        if data['age'] >= 52:
                            if data['cp'] == 2:
                                count_no+=1
                            else:
                                if data['age'] >= 59:
                                    if data['age'] >= 64:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    count_yes+=1
                        else:
                            if data['thal'] == 1:
                                count_yes+=1
                            else:
                                count_no+=1
            else:
                count_yes+=1
        else:
            if data['age'] >= 64:
                if data['sex'] == 0:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                if data['age'] >= 47:
                    if data['cp'] == 3:
                        count_no+=1
                    else:
                        if data['age'] >= 50:
                            count_yes+=1
                        else:
                            if data['cp'] == 1:
                                count_yes+=1
                            else:
                                if data['age'] >= 49:
                                    count_no+=1
                                else:
                                    if data['restecg'] == 1:
                                        count_yes+=1
                                    else:
                                        count_yes+=1
                else:
                    count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['cp'] == 0.0:
        if data['thalach'] >= 182.0:
            count_yes+=1
        else:
            if data['chol'] >= 354.0:
                count_yes+=1
            else:
                if data['oldpeak'] >= 0.6:
                    if data['thalach'] >= 171.0:
                        count_yes+=1
                    else:
                        if data['trestbps'] >= 120.0:
                            if data['exang'] == 0.0:
                                if data['thalach'] >= 138.0:
                                    if data['thalach'] >= 141.0:
                                        if data['age'] >= 60.0:
                                            count_no+=1
                                        else:
                                            if data['oldpeak'] >= 1.2:
                                                count_yes+=1
                                            else:
                                                count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_no+=1
                        else:
                            if data['chol'] >= 275.0:
                                count_no+=1
                            else:
                                count_yes+=1
                else:
                    if data['thalach'] >= 162.0:
                        if data['age'] >= 58.0:
                            count_no+=1
                        else:
                            if data['age'] >= 57.0:
                                count_yes+=1
                            else:
                                count_no+=1
                    else:
                        if data['age'] >= 53.0:
                            if data['thalach'] >= 111.0:
                                if data['exang'] == 0.0:
                                    count_yes+=1
                                else:
                                    if data['age'] >= 63.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_no+=1
    else:
        if data['age'] >= 57.0:
            if data['trestbps'] >= 140.0:
                if data['exang'] == 0.0:
                    if data['chol'] >= 335.0:
                        count_no+=1
                    else:
                        if data['oldpeak'] >= 2.0:
                            if data['cp'] == 2.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_yes+=1
                else:
                    count_no+=1
            else:
                if data['trestbps'] >= 124.0:
                    if data['age'] >= 62.0:
                        if data['age'] >= 64.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['oldpeak'] >= 2.5:
                        count_no+=1
                    else:
                        count_yes+=1
        else:
            if data['oldpeak'] >= 3.6:
                count_no+=1
            else:
                if data['thalach'] >= 195.0:
                    count_no+=1
                else:
                    if data['thalach'] >= 147.0:
                        if data['trestbps'] >= 118.0:
                            count_yes+=1
                        else:
                            if data['cp'] == 2.0:
                                count_yes+=1
                            else:
                                if data['oldpeak'] >= 1.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                    else:
                        if data['oldpeak'] >= 1.4:
                            count_yes+=1
                        else:
                            count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thal'] == 2:
        if data['thalach'] >= 125:
            if data['thalach'] >= 162:
                if data['ca'] == 1:
                    if data['thalach'] >= 164:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['ca'] == 3:
                        count_no+=1
                    else:
                        if data['cp'] == 0:
                            if data['exang'] == 0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
            else:
                if data['thalach'] >= 158:
                    if data['cp'] == 0:
                        count_yes+=1
                    else:
                        if data['exang'] == 0:
                            count_no+=1
                        else:
                            count_yes+=1
                else:
                    if data['ca'] == 1:
                        if data['cp'] == 0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['thalach'] >= 138:
                            if data['cp'] == 2:
                                if data['thalach'] >= 152:
                                    if data['fbs'] == 0:
                                        count_yes+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_yes+=1
                            else:
                                count_yes+=1
                        else:
                            if data['exang'] == 0:
                                count_yes+=1
                            else:
                                count_no+=1
        else:
            if data['cp'] == 0:
                count_no+=1
            else:
                count_yes+=1
    else:
        if data['exang'] == 1:
            if data['thalach'] >= 178:
                count_yes+=1
            else:
                if data['thalach'] >= 109:
                    if data['ca'] == 0:
                        if data['fbs'] == 0:
                            if data['cp'] == 0:
                                if data['thal'] == 3:
                                    count_no+=1
                                else:
                                    if data['thalach'] >= 126:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_no+=1
                else:
                    if data['thalach'] >= 105:
                        if data['thal'] == 1:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
        else:
            if data['thalach'] >= 173:
                if data['thalach'] >= 195:
                    count_no+=1
                else:
                    count_yes+=1
            else:
                if data['ca'] == 4:
                    count_yes+=1
                else:
                    if data['ca'] == 0:
                        if data['thalach'] >= 141:
                            if data['thalach'] >= 147:
                                if data['thalach'] >= 166:
                                    count_no+=1
                                else:
                                    if data['thalach'] >= 161:
                                        count_yes+=1
                                    else:
                                        if data['thalach'] >= 150:
                                            if data['cp'] == 1:
                                                count_yes+=1
                                            else:
                                                count_no+=1
                                        else:
                                            count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['cp'] == 2:
                            if data['thalach'] >= 163:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['ca'] == 0:
        if data['chol'] >= 305:
            if data['chol'] >= 340:
                if data['exang'] == 0:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                if data['cp'] == 1:
                    count_yes+=1
                else:
                    if data['trestbps'] >= 180:
                        if data['age'] >= 64:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['exang'] == 0:
                            if data['chol'] >= 330:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
        else:
            if data['sex'] == 0:
                if data['trestbps'] >= 174:
                    count_no+=1
                else:
                    if data['trestbps'] >= 140:
                        if data['exang'] == 0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['age'] >= 60:
                    if data['cp'] == 1:
                        count_yes+=1
                    else:
                        if data['cp'] == 3:
                            count_yes+=1
                        else:
                            if data['chol'] >= 185:
                                count_no+=1
                            else:
                                if data['exang'] == 0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                else:
                    if data['cp'] == 3:
                        if data['age'] >= 52:
                            if data['chol'] >= 288:
                                if data['age'] >= 59:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_yes+=1
                        else:
                            if data['trestbps'] >= 140:
                                count_yes+=1
                            else:
                                count_no+=1
                    else:
                        if data['trestbps'] >= 150:
                            if data['age'] >= 54:
                                count_yes+=1
                            else:
                                if data['age'] >= 46:
                                    count_no+=1
                                else:
                                    count_yes+=1
                        else:
                            if data['trestbps'] >= 110:
                                if data['chol'] >= 192:
                                    if data['age'] >= 52:
                                        if data['age'] >= 56:
                                            if data['cp'] == 1:
                                                if data['trestbps'] >= 130:
                                                    count_yes+=1
                                                else:
                                                    count_no+=1
                                            else:
                                                count_yes+=1
                                        else:
                                            if data['exang'] == 0:
                                                count_yes+=1
                                            else:
                                                count_no+=1
                                    else:
                                        if data['cp'] == 0:
                                            if data['trestbps'] >= 120:
                                                if data['age'] >= 46:
                                                    count_no+=1
                                                else:
                                                    count_yes+=1
                                            else:
                                                count_yes+=1
                                        else:
                                            count_yes+=1
                                else:
                                    if data['cp'] == 0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                            else:
                                if data['exang'] == 0:
                                    count_no+=1
                                else:
                                    count_yes+=1
    else:
        if data['cp'] == 0:
            if data['sex'] == 0:
                if data['trestbps'] >= 150:
                    count_no+=1
                else:
                    if data['exang'] == 0:
                        count_yes+=1
                    else:
                        count_no+=1
            else:
                count_no+=1
        else:
            if data['age'] >= 54:
                if data['sex'] == 0:
                    if data['trestbps'] >= 140:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['chol'] >= 204:
                        if data['trestbps'] >= 160:
                            if data['cp'] == 1:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1
            else:
                count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['ca'] == 0:
        if data['exang'] == 0:
            if data['trestbps'] >= 120:
                if data['age'] >= 67:
                    if data['age'] >= 70:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['age'] >= 41:
                        if data['sex'] == 0:
                            count_yes+=1
                        else:
                            if data['age'] >= 50:
                                if data['age'] >= 52:
                                    if data['trestbps'] >= 145:
                                        count_yes+=1
                                    else:
                                        if data['trestbps'] >= 124:
                                            if data['age'] >= 64:
                                                count_no+=1
                                            else:
                                                if data['trestbps'] >= 128:
                                                    count_yes+=1
                                                else:
                                                    count_no+=1
                                        else:
                                            count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                    else:
                        if data['age'] >= 40:
                            count_no+=1
                        else:
                            count_yes+=1
            else:
                if data['sex'] == 0:
                    count_yes+=1
                else:
                    if data['age'] >= 47:
                        if data['age'] >= 54:
                            count_yes+=1
                        else:
                            if data['trestbps'] >= 112:
                                count_yes+=1
                            else:
                                count_no+=1
                    else:
                        if data['age'] >= 45:
                            count_no+=1
                        else:
                            if data['age'] >= 41:
                                count_yes+=1
                            else:
                                count_no+=1
        else:
            if data['trestbps'] >= 150:
                count_no+=1
            else:
                if data['trestbps'] >= 130:
                    if data['age'] >= 55:
                        if data['age'] >= 59:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['trestbps'] >= 120:
                        if data['sex'] == 0:
                            if data['age'] >= 63:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['age'] >= 41:
                            count_yes+=1
                        else:
                            count_no+=1
    else:
        if data['age'] >= 54:
            if data['age'] >= 69:
                if data['ca'] == 3:
                    count_no+=1
                else:
                    count_yes+=1
            else:
                if data['ca'] == 4:
                    count_yes+=1
                else:
                    if data['age'] >= 62:
                        if data['sex'] == 0:
                            if data['ca'] == 2:
                                if data['exang'] == 0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                if data['age'] >= 66:
                                    count_yes+=1
                                else:
                                    count_no+=1
                        else:
                            if data['age'] >= 65:
                                count_no+=1
                            else:
                                if data['ca'] == 1:
                                    if data['age'] >= 64:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    count_yes+=1
                    else:
                        if data['sex'] == 1:
                            count_no+=1
                        else:
                            if data['trestbps'] >= 130:
                                count_no+=1
                            else:
                                count_yes+=1
        else:
            if data['trestbps'] >= 130:
                if data['ca'] == 2:
                    count_no+=1
                else:
                    count_yes+=1
            else:
                if data['age'] >= 52:
                    count_no+=1
                else:
                    if data['age'] >= 48:
                        if data['ca'] == 3:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thal'] == 2.0:
        if data['oldpeak'] >= 2.2:
            if data['trestbps'] >= 120.0:
                if data['cp'] == 3.0:
                    count_yes+=1
                else:
                    if data['trestbps'] >= 140.0:
                        count_no+=1
                    else:
                        if data['cp'] == 0.0:
                            count_no+=1
                        else:
                            count_yes+=1
            else:
                count_yes+=1
        else:
            if data['exang'] == 1.0:
                if data['cp'] == 0.0:
                    if data['oldpeak'] >= 0.1:
                        count_no+=1
                    else:
                        if data['trestbps'] >= 138.0:
                            count_yes+=1
                        else:
                            count_no+=1
                else:
                    count_yes+=1
            else:
                if data['restecg'] == 0.0:
                    if data['oldpeak'] >= 0.1:
                        if data['trestbps'] >= 120.0:
                            count_yes+=1
                        else:
                            if data['trestbps'] >= 118.0:
                                count_no+=1
                            else:
                                count_yes+=1
                    else:
                        if data['cp'] == 2.0:
                            count_yes+=1
                        else:
                            if data['trestbps'] >= 130.0:
                                count_no+=1
                            else:
                                if data['trestbps'] >= 128.0:
                                    count_yes+=1
                                else:
                                    count_yes+=1
                else:
                    if data['cp'] == 3.0:
                        if data['trestbps'] >= 140.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['cp'] == 0.0:
                            if data['trestbps'] >= 115.0:
                                count_yes+=1
                            else:
                                if data['oldpeak'] >= 0.1:
                                    count_yes+=1
                                else:
                                    count_no+=1
                        else:
                            count_yes+=1
    else:
        if data['cp'] == 2.0:
            if data['oldpeak'] >= 0.6:
                if data['trestbps'] >= 120.0:
                    count_no+=1
                else:
                    count_yes+=1
            else:
                count_yes+=1
        else:
            if data['cp'] == 3.0:
                if data['restecg'] == 0.0:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                if data['slope'] == 2.0:
                    if data['oldpeak'] >= 2.3:
                        count_yes+=1
                    else:
                        if data['restecg'] == 0.0:
                            count_no+=1
                        else:
                            if data['trestbps'] >= 124.0:
                                if data['trestbps'] >= 132.0:
                                    if data['trestbps'] >= 152.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                if data['trestbps'] >= 108.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                else:
                    if data['oldpeak'] >= 0.9:
                        count_no+=1
                    else:
                        if data['trestbps'] >= 160.0:
                            count_no+=1
                        else:
                            count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thal'] == 2:
        if data['cp'] == 0:
            if data['thalach'] >= 122:
                if data['thalach'] >= 144:
                    if data['thalach'] >= 178:
                        count_yes+=1
                    else:
                        if data['sex'] == 0:
                            if data['thalach'] >= 169:
                                count_no+=1
                            else:
                                if data['slope'] == 1:
                                    if data['restecg'] == 0:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    count_yes+=1
                        else:
                            if data['age'] >= 66:
                                if data['slope'] == 1:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_no+=1
                else:
                    if data['sex'] == 0:
                        count_yes+=1
                    else:
                        count_no+=1
            else:
                count_no+=1
        else:
            if data['thalach'] >= 156:
                if data['age'] >= 64:
                    if data['sex'] == 0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    count_yes+=1
            else:
                if data['thalach'] >= 155:
                    if data['slope'] == 1:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['age'] >= 51:
                        if data['thalach'] >= 152:
                            if data['slope'] == 2:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_yes+=1
                    else:
                        if data['age'] >= 46:
                            count_no+=1
                        else:
                            count_yes+=1
    else:
        if data['cp'] == 0:
            if data['age'] >= 65:
                if data['slope'] == 1:
                    count_no+=1
                else:
                    count_yes+=1
            else:
                if data['thalach'] >= 161:
                    if data['thalach'] >= 162:
                        count_no+=1
                    else:
                        if data['slope'] == 1:
                            count_yes+=1
                        else:
                            count_no+=1
                else:
                    count_no+=1
        else:
            if data['age'] >= 62:
                count_no+=1
            else:
                if data['restecg'] == 0:
                    if data['slope'] == 1:
                        if data['age'] >= 58:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_yes+=1
                else:
                    if data['age'] >= 48:
                        if data['cp'] == 3:
                            count_yes+=1
                        else:
                            if data['cp'] == 1:
                                count_no+=1
                            else:
                                if data['slope'] == 1:
                                    count_no+=1
                                else:
                                    count_yes+=1
                    else:
                        if data['age'] >= 40:
                            count_yes+=1
                        else:
                            count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['ca'] == 0.0:
        if data['oldpeak'] >= 3.0:
            if data['age'] >= 55.0:
                count_no+=1
            else:
                count_yes+=1
        else:
            if data['cp'] == 0.0:
                if data['age'] >= 42.0:
                    if data['trestbps'] >= 124.0:
                        if data['chol'] >= 270.0:
                            count_no+=1
                        else:
                            if data['exang'] == 0.0:
                                count_yes+=1
                            else:
                                if data['age'] >= 59.0:
                                    count_no+=1
                                else:
                                    if data['chol'] >= 207.0:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                    else:
                        if data['oldpeak'] >= 0.8:
                            if data['age'] >= 46.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_yes+=1
                else:
                    count_no+=1
            else:
                if data['age'] >= 64.0:
                    if data['oldpeak'] >= 0.2:
                        if data['age'] >= 67.0:
                            if data['chol'] >= 212.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['trestbps'] >= 112.0:
                        count_yes+=1
                    else:
                        if data['chol'] >= 243.0:
                            count_no+=1
                        else:
                            if data['oldpeak'] >= 1.0:
                                if data['cp'] == 1.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_yes+=1
    else:
        if data['age'] >= 69.0:
            if data['ca'] == 3.0:
                count_no+=1
            else:
                count_yes+=1
        else:
            if data['exang'] == 1.0:
                if data['trestbps'] >= 108.0:
                    if data['cp'] == 1.0:
                        if data['ca'] == 1.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_no+=1
                else:
                    count_yes+=1
            else:
                if data['trestbps'] >= 140.0:
                    if data['cp'] == 0.0:
                        count_no+=1
                    else:
                        if data['trestbps'] >= 154.0:
                            count_no+=1
                        else:
                            count_yes+=1
                else:
                    if data['trestbps'] >= 110.0:
                        if data['ca'] == 4.0:
                            count_yes+=1
                        else:
                            if data['age'] >= 64.0:
                                if data['age'] >= 65.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                if data['chol'] >= 234.0:
                                    count_no+=1
                                else:
                                    if data['trestbps'] >= 130.0:
                                        if data['ca'] == 2.0:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                                    else:
                                        count_no+=1
                    else:
                        count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['ca'] == 0:
        if data['exang'] == 1:
            if data['trestbps'] >= 145:
                if data['chol'] >= 249:
                    count_no+=1
                else:
                    count_yes+=1
            else:
                if data['thal'] == 2:
                    if data['chol'] >= 211:
                        count_yes+=1
                    else:
                        if data['chol'] >= 197:
                            count_no+=1
                        else:
                            count_yes+=1
                else:
                    if data['chol'] >= 241:
                        count_no+=1
                    else:
                        if data['chol'] >= 199:
                            count_yes+=1
                        else:
                            count_no+=1
        else:
            if data['age'] >= 48:
                if data['sex'] == 1:
                    if data['chol'] >= 261:
                        if data['chol'] >= 302:
                            count_yes+=1
                        else:
                            if data['thal'] == 2:
                                if data['chol'] >= 273:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_no+=1
                    else:
                        if data['age'] >= 60:
                            if data['age'] >= 62:
                                if data['age'] >= 67:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                else:
                    if data['chol'] >= 330:
                        if data['chol'] >= 340:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1
            else:
                count_yes+=1
    else:
        if data['thal'] == 2:
            if data['ca'] == 3:
                count_no+=1
            else:
                if data['sex'] == 0:
                    if data['age'] >= 60:
                        count_yes+=1
                    else:
                        if data['chol'] >= 319:
                            count_no+=1
                        else:
                            count_yes+=1
                else:
                    if data['trestbps'] >= 125:
                        if data['age'] >= 61:
                            if data['trestbps'] >= 160:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
        else:
            if data['trestbps'] >= 110:
                count_no+=1
            else:
                if data['chol'] >= 234:
                    count_no+=1
                else:
                    count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['cp'] == 0:
        if data['trestbps'] >= 110:
            if data['age'] >= 71:
                count_yes+=1
            else:
                if data['age'] >= 44:
                    if data['trestbps'] >= 120:
                        if data['trestbps'] >= 134:
                            if data['age'] >= 55:
                                count_no+=1
                            else:
                                if data['age'] >= 51:
                                    if data['restecg'] == 1:
                                        if data['age'] >= 54:
                                            count_yes+=1
                                        else:
                                            count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_no+=1
                        else:
                            if data['trestbps'] >= 132:
                                if data['age'] >= 57:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                if data['sex'] == 1:
                                    if data['age'] >= 66:
                                        if data['age'] >= 67:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    if data['restecg'] == 2:
                                        count_no+=1
                                    else:
                                        if data['age'] >= 63:
                                            if data['age'] >= 64:
                                                count_yes+=1
                                            else:
                                                count_no+=1
                                        else:
                                            count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['age'] >= 42:
                        if data['restecg'] == 0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
        else:
            if data['trestbps'] >= 102:
                if data['trestbps'] >= 108:
                    if data['sex'] == 0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_yes+=1
            else:
                count_no+=1
    else:
        if data['sex'] == 0:
            if data['cp'] == 1:
                if data['age'] >= 57:
                    if data['age'] >= 63:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    count_yes+=1
            else:
                count_yes+=1
        else:
            if data['trestbps'] >= 125:
                if data['age'] >= 60:
                    if data['age'] >= 70:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['age'] >= 57:
                        if data['trestbps'] >= 140:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['trestbps'] >= 150:
                            if data['age'] >= 52:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
            else:
                if data['trestbps'] >= 108:
                    if data['age'] >= 45:
                        if data['age'] >= 51:
                            if data['age'] >= 57:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thalach'] >= 145.0:
        if data['thal'] == 3.0:
            if data['trestbps'] >= 172.0:
                if data['slope'] == 1.0:
                    count_no+=1
                else:
                    count_yes+=1
            else:
                if data['oldpeak'] >= 1.9:
                    count_no+=1
                else:
                    if data['trestbps'] >= 140.0:
                        if data['oldpeak'] >= 1.6:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['trestbps'] >= 118.0:
                            if data['chol'] >= 254.0:
                                if data['trestbps'] >= 125.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_yes+=1
                        else:
                            if data['oldpeak'] >= 1.0:
                                count_no+=1
                            else:
                                if data['chol'] >= 211.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
        else:
            if data['oldpeak'] >= 3.6:
                count_no+=1
            else:
                if data['trestbps'] >= 120.0:
                    if data['thalach'] >= 148.0:
                        if data['trestbps'] >= 154.0:
                            if data['trestbps'] >= 155.0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            if data['oldpeak'] >= 0.8:
                                if data['trestbps'] >= 138.0:
                                    count_yes+=1
                                else:
                                    if data['trestbps'] >= 134.0:
                                        count_no+=1
                                    else:
                                        if data['slope'] == 1.0:
                                            if data['chol'] >= 284.0:
                                                count_no+=1
                                            else:
                                                count_yes+=1
                                        else:
                                            count_yes+=1
                            else:
                                count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['trestbps'] >= 112.0:
                        count_no+=1
                    else:
                        if data['thal'] == 1.0:
                            count_no+=1
                        else:
                            count_yes+=1
    else:
        if data['slope'] == 2.0:
            if data['trestbps'] >= 128.0:
                if data['thal'] == 3.0:
                    count_no+=1
                else:
                    count_yes+=1
            else:
                if data['trestbps'] >= 112.0:
                    count_no+=1
                else:
                    count_yes+=1
        else:
            if data['trestbps'] >= 120.0:
                if data['thalach'] >= 144.0:
                    if data['chol'] >= 249.0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['chol'] >= 303.0:
                        if data['chol'] >= 305.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['oldpeak'] >= 0.1:
                            count_no+=1
                        else:
                            if data['trestbps'] >= 160.0:
                                count_no+=1
                            else:
                                if data['trestbps'] >= 135.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
            else:
                if data['chol'] >= 206.0:
                    if data['trestbps'] >= 110.0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['exang'] == 0.0:
        if data['oldpeak'] >= 3.6:
            count_no+=1
        else:
            if data['trestbps'] >= 164.0:
                if data['chol'] >= 283.0:
                    count_no+=1
                else:
                    if data['trestbps'] >= 170.0:
                        count_yes+=1
                    else:
                        count_no+=1
            else:
                if data['age'] >= 57.0:
                    if data['trestbps'] >= 125.0:
                        if data['chol'] >= 204.0:
                            if data['trestbps'] >= 140.0:
                                if data['oldpeak'] >= 0.2:
                                    if data['chol'] >= 269.0:
                                        count_yes+=1
                                    else:
                                        if data['slope'] == 1.0:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                                else:
                                    if data['age'] >= 67.0:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['age'] >= 60.0:
                            count_yes+=1
                        else:
                            if data['chol'] >= 248.0:
                                count_yes+=1
                            else:
                                count_no+=1
                else:
                    if data['trestbps'] >= 125.0:
                        if data['slope'] == 1.0:
                            if data['restecg'] == 1.0:
                                if data['trestbps'] >= 140.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_yes+=1
                        else:
                            count_yes+=1
                    else:
                        if data['trestbps'] >= 124.0:
                            count_no+=1
                        else:
                            if data['age'] >= 45.0:
                                count_yes+=1
                            else:
                                if data['restecg'] == 0.0:
                                    count_no+=1
                                else:
                                    if data['age'] >= 41.0:
                                        count_yes+=1
                                    else:
                                        count_no+=1
    else:
        if data['trestbps'] >= 108.0:
            if data['oldpeak'] >= 0.6:
                if data['fbs'] == 0.0:
                    if data['chol'] >= 354.0:
                        count_yes+=1
                    else:
                        if data['age'] >= 64.0:
                            if data['trestbps'] >= 145.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            if data['slope'] == 0.0:
                                if data['trestbps'] >= 142.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_no+=1
                else:
                    if data['trestbps'] >= 150.0:
                        if data['trestbps'] >= 178.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
            else:
                if data['oldpeak'] >= 0.2:
                    count_yes+=1
                else:
                    if data['age'] >= 57.0:
                        if data['chol'] >= 207.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_no+=1
        else:
            count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thal'] == 2.0:
        if data['oldpeak'] >= 1.4:
            if data['ca'] == 0.0:
                if data['cp'] == 0.0:
                    count_no+=1
                else:
                    if data['oldpeak'] >= 3.0:
                        if data['oldpeak'] >= 3.5:
                            if data['oldpeak'] >= 3.6:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['fbs'] == 1.0:
                    count_no+=1
                else:
                    if data['cp'] == 0.0:
                        if data['exang'] == 0.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1
        else:
            if data['exang'] == 0.0:
                if data['ca'] == 1.0:
                    if data['cp'] == 0.0:
                        count_yes+=1
                    else:
                        if data['cp'] == 1.0:
                            if data['oldpeak'] >= 0.8:
                                count_yes+=1
                            else:
                                count_yes+=1
                        else:
                            count_yes+=1
                else:
                    if data['cp'] == 3.0:
                        if data['ca'] == 0.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['oldpeak'] >= 0.1:
                            count_yes+=1
                        else:
                            if data['cp'] == 2.0:
                                if data['ca'] == 0.0:
                                    count_yes+=1
                                else:
                                    count_yes+=1
                            else:
                                if data['cp'] == 0.0:
                                    count_yes+=1
                                else:
                                    count_yes+=1
            else:
                if data['cp'] == 0.0:
                    if data['ca'] == 0.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    count_yes+=1
    else:
        if data['cp'] == 2.0:
            if data['oldpeak'] >= 0.6:
                if data['fbs'] == 0.0:
                    if data['oldpeak'] >= 3.2:
                        count_no+=1
                    else:
                        if data['oldpeak'] >= 1.6:
                            if data['exang'] == 0.0:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            if data['exang'] == 0.0:
                                count_no+=1
                            else:
                                count_yes+=1
                else:
                    count_no+=1
            else:
                count_yes+=1
        else:
            if data['thal'] == 1.0:
                if data['ca'] == 0.0:
                    count_yes+=1
                else:
                    count_no+=1
            else:
                if data['ca'] == 4.0:
                    count_yes+=1
                else:
                    if data['oldpeak'] >= 0.3:
                        if data['cp'] == 3.0:
                            if data['fbs'] == 0.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['ca'] == 1.0:
                            count_yes+=1
                        else:
                            if data['exang'] == 0.0:
                                count_no+=1
                            else:
                                if data['ca'] == 0.0:
                                    count_yes+=1
                                else:
                                    count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thal'] == 2.0:
        if data['oldpeak'] >= 3.2:
            count_no+=1
        else:
            if data['age'] >= 57.0:
                if data['sex'] == 0.0:
                    if data['age'] >= 64.0:
                        count_yes+=1
                    else:
                        if data['age'] >= 59.0:
                            if data['fbs'] == 0.0:
                                if data['ca'] == 0.0:
                                    if data['age'] >= 63.0:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_yes+=1
                        else:
                            count_yes+=1
                else:
                    if data['ca'] == 0.0:
                        if data['age'] >= 64.0:
                            count_no+=1
                        else:
                            if data['oldpeak'] >= 1.6:
                                count_yes+=1
                            else:
                                count_yes+=1
                    else:
                        if data['age'] >= 69.0:
                            count_yes+=1
                        else:
                            count_no+=1
            else:
                if data['ca'] == 3.0:
                    if data['oldpeak'] >= 0.8:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['ca'] == 1.0:
                        if data['oldpeak'] >= 0.3:
                            count_yes+=1
                        else:
                            if data['sex'] == 0.0:
                                count_yes+=1
                            else:
                                count_no+=1
                    else:
                        count_yes+=1
    else:
        if data['ca'] == 0.0:
            if data['oldpeak'] >= 0.8:
                if data['thal'] == 3.0:
                    if data['oldpeak'] >= 4.2:
                        if data['oldpeak'] >= 5.6:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['fbs'] == 1.0:
                            if data['oldpeak'] >= 1.6:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                else:
                    if data['oldpeak'] >= 2.8:
                        count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['sex'] == 0.0:
                    count_no+=1
                else:
                    if data['age'] >= 41.0:
                        if data['oldpeak'] >= 0.5:
                            if data['fbs'] == 0.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
        else:
            if data['fbs'] == 0.0:
                if data['age'] >= 53.0:
                    if data['age'] >= 62.0:
                        if data['age'] >= 65.0:
                            count_no+=1
                        else:
                            if data['oldpeak'] >= 1.2:
                                if data['ca'] == 3.0:
                                    if data['sex'] == 0.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['ca'] == 1.0:
                        count_yes+=1
                    else:
                        count_no+=1
            else:
                if data['oldpeak'] >= 0.6:
                    count_no+=1
                else:
                    count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['exang'] == 0:
        if data['ca'] == 2:
            if data['chol'] >= 244:
                if data['restecg'] == 0:
                    if data['chol'] >= 293:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_yes+=1
            else:
                count_no+=1
        else:
            if data['ca'] == 3:
                count_no+=1
            else:
                if data['ca'] == 1:
                    if data['restecg'] == 1:
                        if data['chol'] >= 201:
                            if data['chol'] >= 203:
                                if data['chol'] >= 242:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['fbs'] == 0:
                            count_no+=1
                        else:
                            if data['chol'] >= 282:
                                count_no+=1
                            else:
                                count_yes+=1
                else:
                    if data['chol'] >= 262:
                        if data['chol'] >= 335:
                            if data['chol'] >= 342:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['chol'] >= 261:
                            count_no+=1
                        else:
                            if data['chol'] >= 245:
                                count_yes+=1
                            else:
                                if data['chol'] >= 223:
                                    if data['restecg'] == 0:
                                        count_yes+=1
                                    else:
                                        if data['chol'] >= 235:
                                            if data['chol'] >= 237:
                                                if data['chol'] >= 240:
                                                    if data['chol'] >= 243:
                                                        count_no+=1
                                                    else:
                                                        count_yes+=1
                                                else:
                                                    count_no+=1
                                            else:
                                                count_yes+=1
                                        else:
                                            count_no+=1
                                else:
                                    if data['restecg'] == 0:
                                        if data['chol'] >= 186:
                                            if data['chol'] >= 212:
                                                if data['chol'] >= 219:
                                                    count_yes+=1
                                                else:
                                                    count_no+=1
                                            else:
                                                count_yes+=1
                                        else:
                                            if data['chol'] >= 185:
                                                count_no+=1
                                            else:
                                                count_yes+=1
                                    else:
                                        count_yes+=1
    else:
        if data['ca'] == 0:
            if data['chol'] >= 199:
                if data['chol'] >= 244:
                    if data['restecg'] == 1:
                        if data['chol'] >= 325:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['chol'] >= 274:
                            count_no+=1
                        else:
                            count_yes+=1
                else:
                    if data['fbs'] == 0:
                        if data['chol'] >= 231:
                            if data['chol'] >= 240:
                                count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                    else:
                        if data['chol'] >= 243:
                            count_yes+=1
                        else:
                            count_no+=1
            else:
                count_no+=1
        else:
            if data['ca'] == 1:
                if data['chol'] >= 263:
                    if data['restecg'] == 0:
                        if data['chol'] >= 269:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['chol'] >= 269:
                            count_no+=1
                        else:
                            count_yes+=1
                else:
                    if data['chol'] >= 239:
                        count_no+=1
                    else:
                        if data['chol'] >= 213:
                            count_yes+=1
                        else:
                            count_no+=1
            else:
                count_no+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['thal'] == 2.0:
        if data['ca'] == 0.0:
            if data['exang'] == 0.0:
                if data['oldpeak'] >= 3.6:
                    count_no+=1
                else:
                    if data['chol'] >= 330.0:
                        if data['chol'] >= 342.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['slope'] == 1.0:
                            if data['oldpeak'] >= 1.0:
                                if data['chol'] >= 245.0:
                                    count_yes+=1
                                else:
                                    if data['chol'] >= 237.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                            else:
                                count_yes+=1
                        else:
                            count_yes+=1
            else:
                if data['chol'] >= 244.0:
                    if data['chol'] >= 268.0:
                        count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['chol'] >= 208.0:
                        count_yes+=1
                    else:
                        if data['chol'] >= 197.0:
                            count_no+=1
                        else:
                            count_yes+=1
        else:
            if data['oldpeak'] >= 2.6:
                count_no+=1
            else:
                if data['chol'] >= 230.0:
                    if data['chol'] >= 239.0:
                        if data['chol'] >= 290.0:
                            if data['chol'] >= 302.0:
                                if data['ca'] == 2.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['slope'] == 1.0:
                        count_no+=1
                    else:
                        count_yes+=1
    else:
        if data['thal'] == 0.0:
            if data['chol'] >= 216.0:
                count_yes+=1
            else:
                count_no+=1
        else:
            if data['ca'] == 4.0:
                count_yes+=1
            else:
                if data['chol'] >= 164.0:
                    if data['ca'] == 0.0:
                        if data['oldpeak'] >= 0.3:
                            if data['chol'] >= 243.0:
                                if data['chol'] >= 298.0:
                                    if data['chol'] >= 307.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                if data['exang'] == 1.0:
                                    if data['chol'] >= 201.0:
                                        if data['chol'] >= 217.0:
                                            count_no+=1
                                        else:
                                            count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    if data['slope'] == 0.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                        else:
                            if data['chol'] >= 282.0:
                                if data['chol'] >= 309.0:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                count_yes+=1
                    else:
                        if data['oldpeak'] >= 1.9:
                            count_no+=1
                        else:
                            if data['ca'] == 3.0:
                                if data['oldpeak'] >= 1.8:
                                    count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                if data['chol'] >= 277.0:
                                    if data['chol'] >= 283.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_no+=1
                else:
                    count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

    if data['oldpeak'] >= 1.8:
        if data['age'] >= 64.0:
            if data['oldpeak'] >= 2.4:
                count_no+=1
            else:
                if data['ca'] == 3.0:
                    count_no+=1
                else:
                    count_yes+=1
        else:
            if data['age'] >= 53.0:
                if data['ca'] == 0.0:
                    if data['age'] >= 59.0:
                        if data['age'] >= 60.0:
                            count_no+=1
                        else:
                            count_yes+=1
                    else:
                        count_no+=1
                else:
                    if data['oldpeak'] >= 1.9:
                        count_no+=1
                    else:
                        if data['restecg'] == 0.0:
                            count_no+=1
                        else:
                            count_yes+=1
            else:
                if data['ca'] == 1.0:
                    count_yes+=1
                else:
                    if data['age'] >= 51.0:
                        count_yes+=1
                    else:
                        count_no+=1
    else:
        if data['ca'] == 0.0:
            if data['slope'] == 0.0:
                if data['age'] >= 48.0:
                    if data['oldpeak'] >= 1.0:
                        count_no+=1
                    else:
                        count_yes+=1
                else:
                    count_yes+=1
            else:
                if data['restecg'] == 0.0:
                    if data['age'] >= 44.0:
                        if data['oldpeak'] >= 1.0:
                            count_yes+=1
                        else:
                            if data['oldpeak'] >= 0.8:
                                if data['age'] >= 65.0:
                                    if data['age'] >= 67.0:
                                        count_no+=1
                                    else:
                                        count_yes+=1
                                else:
                                    count_no+=1
                            else:
                                if data['age'] >= 59.0:
                                    if data['age'] >= 66.0:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    if data['oldpeak'] >= 0.5:
                                        if data['age'] >= 48.0:
                                            if data['age'] >= 51.0:
                                                count_yes+=1
                                            else:
                                                count_no+=1
                                        else:
                                            count_yes+=1
                                    else:
                                        count_yes+=1
                    else:
                        count_yes+=1
                else:
                    if data['age'] >= 51.0:
                        if data['oldpeak'] >= 1.4:
                            count_no+=1
                        else:
                            if data['slope'] == 1.0:
                                if data['oldpeak'] >= 1.1:
                                    count_yes+=1
                                else:
                                    if data['age'] >= 63.0:
                                        count_no+=1
                                    else:
                                        if data['age'] >= 59.0:
                                            if data['oldpeak'] >= 0.5:
                                                count_yes+=1
                                            else:
                                                count_no+=1
                                        else:
                                            count_no+=1
                            else:
                                if data['oldpeak'] >= 0.3:
                                    if data['oldpeak'] >= 0.4:
                                        count_yes+=1
                                    else:
                                        count_no+=1
                                else:
                                    count_yes+=1
                    else:
                        if data['age'] >= 41.0:
                            count_yes+=1
                        else:
                            if data['age'] >= 40.0:
                                count_no+=1
                            else:
                                count_yes+=1
        else:
            if data['slope'] == 1.0:
                if data['age'] >= 45.0:
                    if data['ca'] == 4.0:
                        count_yes+=1
                    else:
                        if data['age'] >= 64.0:
                            if data['age'] >= 67.0:
                                count_no+=1
                            else:
                                count_yes+=1
                        else:
                            count_no+=1
                else:
                    if data['restecg'] == 0.0:
                        count_no+=1
                    else:
                        count_yes+=1
            else:
                if data['oldpeak'] >= 0.2:
                    if data['ca'] == 2.0:
                        if data['restecg'] == 0.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        count_yes+=1
                else:
                    if data['restecg'] == 0.0:
                        if data['ca'] == 3.0:
                            count_yes+=1
                        else:
                            count_no+=1
                    else:
                        if data['age'] >= 58.0:
                            if data['age'] >= 60.0:
                                if data['age'] >= 61.0:
                                    count_no+=1
                                else:
                                    count_yes+=1
                            else:
                                count_no+=1
                        else:
                            count_yes+=1

    if count_yes >= count_no: return 1
    else: return 0

