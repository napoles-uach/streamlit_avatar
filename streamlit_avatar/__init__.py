# streamlit_avatar/__init__.py

import streamlit as st
import streamlit.components.v1 as components

def avatar(text='',lang='en-US'):
    try:
        texto_usuario = text

        # Generación de los keyframes para la animación CSS.
        keyframes = "".join([f"{i*2}% {{background-image: url('https://raw.githubusercontent.com/napoles-uach/streamlit_avatar/main/artic_{i}.png');}}\n" for i in range(2)])

       # keyframes = "".join([f"{i*10}% {{background-image: url('https://raw.githubusercontent.com/napoles-uach/streamlit_avatar/main/robot{i+1}.png');}}\n" for i in range(10)])

        html_str = f"""
        <html>
        <head>
            <meta charset="utf-8">
            <title>Animated Speaking Avatar</title>
            <style>
                body {{
                    background: black;
                    color: white;
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }}
                .avatar {{
                    width: 150px;
                    height: 150px;
                    background-size: cover;
                    background-image: url('https://raw.githubusercontent.com/napoles-uach/streamlit_avatar/main/robot1.png');
                }}
                @keyframes speakAnimation {{
                    {keyframes}
                }}
            </style>
        </head>
        <body>
            <div class="avatar" id="avatar"></div>
            <script>
                document.addEventListener('DOMContentLoaded', (event) => {{
                    var avatar = document.getElementById("avatar");
                    avatar.style.animation = "none"; // Reinicia la animación
                    setTimeout(() => {{
                        avatar.style.animation = "speakAnimation 2s steps(9, end) infinite";
                    }}, 50);

                    var texto = `{texto_usuario}`;
                    var utterance = new SpeechSynthesisUtterance(texto);
                    utterance.lang = "{lang}"; // Configurar el idioma deseado
                    utterance.onend = function(event) {{
                        setTimeout(() => {{ avatar.style.animation = "none"; }}, 500);
                    }};
                    speechSynthesis.speak(utterance);
                }});
            </script>
        </body>
        </html>
        """

        components.html(html_str, height=300)
    except:
        pass
