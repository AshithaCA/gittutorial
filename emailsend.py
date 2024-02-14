import smtplib
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('sakurasiya26@gmail.com','sdqe trby ytdx pzls')
message='hai i am sakura'
s.sendmail('sakurasiya26@gmail.com','ashithali321@gmail.com',message)
s.quit()