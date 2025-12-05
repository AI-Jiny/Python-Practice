from string.templatelib import Template, Interpolation
import html

def test_tstring(user_input):
    """
    Docstring for test_tstring
    
    :param user_input: Description
    """
    ## f-string 사용시
    html = f"<p>{user_input}</p>"
    print("f-string 결과")
    print(type(html))
    print(html)

    ## t-string 사용시 str대신 Template 객체를 반환하고 사용자 입력이 Interpolation으로 구분됨
    html2 = t"<p>{user_input}</p>"
    print("t-string 결과")
    print(html2)        #Template(strings=('<p>', '</p>'), interpolations=(Interpolation("<script>alert('XSS');</script>", 'user_input', None, ''),))
    print(type(html2))  #<class 'string.templatelib.Template'>
    print([p for p in html2]) # ['<p>', Interpolation("<script>alert('XSS');</script>", 'user_input', None, ''), '</p>'

def main():

    ## t-string test
    user_input = "<script>alert('XSS');</script>"
    test_tstring(user_input)


if __name__ == "__main__":
    main()
