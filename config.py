answer_examples = [
    {
        "input": "날짜를 포맷팅하는 함수가 있나요?", 
        "answer": "네! **formatDate** 함수를 추천드립니다. dayjs를 사용해서 다양한 형식으로 날짜를 포맷팅할 수 있습니다.\n\n```typescript\nformatDate('2023-12-25', 'YYYY년 MM월 DD일')\n// 출력: '2023년 12월 25일'\n```"
    },
    {
        "input": "숫자만 입력받는 input 만들고 싶어요",
        "answer": "**convertNumericInput** 함수를 사용하세요! 숫자가 아닌 문자는 자동으로 필터링해줍니다.\n\n```typescript\nconst [value, setValue] = useState('');\n<input onChange={convertNumericInput(setValue)} />\n```"
    },
    {
        "input": "천단위 콤마 붙이는 함수 있나요?",
        "answer": "**formatNumberToLocaleStringWithDecimals** 함수를 추천합니다! 소수점 처리 방식도 선택할 수 있어요.\n\n```typescript\nformatNumberToLocaleStringWithDecimals(1234.567)\n// 출력: '1,234.56'\n```"
    },
    {
        "input": "휴대폰 번호에 하이픈 넣고 싶어요",
        "answer": "**formatPhoneNumber** 함수를 사용하시면 됩니다! 000-0000-0000 형식으로 자동 포맷팅해줍니다.\n\n```typescript\nformatPhoneNumber('01012345678')\n// 출력: '010-1234-5678'\n```"
    },
    {
        "input": "react-hook-form에서 변경된 필드만 가져오려면?",
        "answer": "**getChangedFormFields** 함수가 딱 맞습니다! dirtyFields와 formValues를 넘겨주면 변경된 필드만 추출해줍니다.\n\n```typescript\nconst changedData = getChangedFormFields(dirtyFields, getValues())\n```"
    },
    {
        "input": "시간을 분으로 바꾸는 함수?",
        "answer": "**convertTimeToMinutes** 함수를 사용하세요! HH:mm 형식을 분 단위로 변환합니다.\n\n```typescript\nconvertTimeToMinutes('02:30')\n// 출력: 150\n```"
    },
    {
        "input": "팝업창을 화면 가운데 띄우고 싶어요",
        "answer": "**getWindowPopupCenter** 함수를 추천합니다! 화면 크기에 관계없이 정확한 중앙에 팝업을 배치해줍니다.\n\n```typescript\nconst options = getWindowPopupCenter({popupWidth: 600, popupHeight: 400});\nwindow.open(url, 'popup', options);\n```"
    },
    {
        "input": "숫자 입력 검증하는 방법?",
        "answer": "**validateNumericInput** 함수로 zod 스키마를 만들 수 있습니다! 빈값, 숫자 형식, 0보다 큰 값을 한번에 검증합니다.\n\n```typescript\nconst schema = validateNumericInput('나이');\nschema.parse('25'); // 통과\n```"
    }
]