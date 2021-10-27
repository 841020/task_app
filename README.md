# task_app

## <a href="https://infinite-journey-31500.herokuapp.com/">Demo server on Heroku</a>
## <a href="https://github.com/841020/task_app/blob/main/api_example.md">API example</a>

<p>docker pull and docker run</p>
<pre><code>$sudo docker pull ghcr.io/841020/task_app:main</code></pre>
<pre><code>$sudo docker run --publish 8000:8000 {image id}</code></pre>
<p>then you can test task_app on 127.0.0.1:8000 from website</p>
<p>if you don't want to init your server data every time, your should volumes out sample.db from task_app container</p>

# Follow here for local development or testing

<p>local unittest</p>
<pre><code>$cd web</code></pre>
<pre><code>$coverage run -m unittest discover</code></pre>
<p>check coverage report</p>
<pre><code>$coverage report -m</code></pre>

<p>debug mode development in local without gunicorn server</p>
<pre><code>$cd web</code></pre>
<pre><code>$export FLASK_APP="app:create_app()"</code></pre>
<pre><code>$export FLASK_ENV=development</code></pre>
<pre><code>$flask run --port 8000</code></pre>
