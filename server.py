import asyncio
import time
from urllib.parse import unquote_plus

async def handle_client(reader, writer):
    try:
        request = await reader.read(100)
        request = request.decode()

        if not request:
            writer.close()
            await writer.wait_closed()
            return

        method, path = request.split()[:2]

        if method == 'GET' :
            if path == '/':
                #server homepage
                with open("templates/index.html", "r") as file:
                    content = file.read()
                    await send_response(writer, '200 OK', content, )
        
            elif path == '/register':
                #serve registration form
                with open("templates/register.html", "r") as file:
                    content = file.read()
                    await send_response(writer, '200 OK', content, )
                    
            elif path.startswith('/assets/'):
                local_path = path.lstrip('/')
                with open(local_path, "rb") as file:
                    content = file.read()
                    await send_response(writer, '200 OK', content, content_type='image/jpeg')
            else:
                content = " <h1>Page Not Found</h1>"
                await send_response(writer, '404 Not Found', content, )
            
        elif method == 'POST' and path == '/submit':
            raw_data = await reader.read(2048)
            _ , form_data = raw_data.decode().split('\r\n\r\n', 1)

            username = email = ''
            for pair in form_data.split('&'):
                if not pair:
                    continue
                key, val = pair.split('=', 1)
                val = unquote_plus(val)

                if key == 'username':
                    username = val
                elif key == 'email':
                    email = val

            with open('db.txt', 'w') as file:
                file.write(f"{username} {email}\n")

            success_code = "<h1>Registration Successful</h1>"
            await send_response(writer, '200 OK', success_code, content_type='text/html')

        else:
            failure_code = "<h1>Registrationn Failed</h1>"
            await send_response(writer, '200 OK', failure_code, )

        
    except Exception as e:
        print(e)

    finally:
        # print(request)
        writer.close()
        await writer.wait_closed()

async def send_response(writer, status, content, content_type='text/html'):
    local = time.localtime()
    ftime = time.strftime("%a, %d %B %Y %H:%M:%S GMT", local)

    if  isinstance(content, str):
        content = content.encode()

    headers = (
        f"HTTP/1.1 {status}\r\n"
        f"Date: {ftime}\r\n"
        f"Server: yewo_tech_ltd/2.4\r\n"
        f"Content-Type: {content_type}; charset=UTF-8\r\n"
        f"Content-Length: {len(content)}\r\n"
        f"\r\n"
    ).encode()

    writer.write(headers + content)
    await writer.drain()


async def main():
    server = await asyncio.start_server(handle_client, 'localhost' , 8085)

    addr = server.sockets[0].getsockname()
    print(f"server running on {addr}")

    async with server:
         await server.serve_forever()

asyncio.run(main())