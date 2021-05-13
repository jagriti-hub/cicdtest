FROM 280111790906.dkr.ecr.us-east-1.amazonaws.com/python3:latest
RUN addgroup --system --gid 150 app && adduser --system --ingroup app --uid 150 app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME
RUN apt-get update
ADD code $APP_HOME
COPY code/requirement.txt  $APP_HOME/requirement.txt
RUN pip install --upgrade pip -r requirement.txt
RUN chown -R app:app $APP_HOME
USER app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
