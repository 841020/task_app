# task_app

<p>local unittest</p>
<pre><code>$cd web</code></pre>
<pre><code>$coverage run -m unittest discover</code></pre>
<p>check coverage report</p>
<pre><code>$coverage report -m</code></pre>

<p>local test without gunicorn server</p>
<pre><code>$cd web</code></pre>
<pre><code>$export FLASK_APP="app:create_app()"</code></pre>
<pre><code>$flask run --port 8000</code></pre>

<p>run with docker-compose</p>
<pre><code>$cd task_app</code></pre>
<pre><code>$sudo docker-compose up</code></pre>
