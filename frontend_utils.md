# Frontend 유틸 함수 라이브러리

## 1. 날짜 포맷팅 함수 (formatDate)

**목적**: 날짜를 지정된 형식으로 포맷팅하며, dayjs 라이브러리를 사용하여 다양한 로케일 지원

**함수명**: `formatDate`

**매개변수**:

- `date` (DateType): 포맷팅할 날짜 (Date 객체, ISO 문자열, 타임스탬프 등 dayjs에서 지원하는 형식)
- `format` (Format): 날짜 포맷 문자열 (예: 'YYYY/MM/DD(ddd) HH:mm')
- `locale` (Locale, 기본값: 'ko'): 로케일 설정 ('ko' 또는 'en')

**반환값**: 포맷팅된 날짜 문자열 또는 undefined (날짜가 유효하지 않은 경우)

**사용 예시**:

```typescript
import { formatDate } from "@/utils/date";

// 기본 사용법 (한국어 로케일 자동 적용)
console.log(formatDate("2023-12-25", "YYYY년 MM월 DD일"));
// 출력: '2023년 12월 25일'

// 날짜와 시간 표시
console.log(formatDate("2023-12-25T15:30:00", "YYYY/MM/DD(ddd) HH:mm"));
// 출력: '2023/12/25(월) 15:30'

// locale 지정
console.log(formatDate("2023-12-25", "YYYY/MM/DD(ddd)", "en"));
// 출력: '2023/12/25(Mon)'

// undefined 처리
console.log(formatDate(undefined, "YYYY/MM/DD"));
// 출력: undefined
```

**키워드**: 날짜, 포맷, dayjs, locale, 한국어, date format, i18n

---

## 2. 날짜 유효성 검사 함수 (isValidDate)

**목적**: 주어진 날짜가 유효한 날짜인지 확인

**함수명**: `isValidDate`

**매개변수**:

- `date` (DateType): 확인할 날짜 객체 또는 문자열

**반환값**: 유효한 날짜인 경우 true, 그렇지 않으면 false

**사용 예시**:

```typescript
import { isValidDate } from "@/utils/date";

// 유효한 날짜 확인
console.log(isValidDate("2023-12-25"));
// 출력: true

console.log(isValidDate(new Date()));
// 출력: true

// 유효하지 않은 날짜
console.log(isValidDate("2023-13-40"));
// 출력: false

// undefined 처리
console.log(isValidDate(undefined));
// 출력: false

console.log(isValidDate(null));
// 출력: false
```

**키워드**: 날짜, 유효성, 검증, validation, date validation

---

## 3. 날짜 형식 검사 함수 (isCheckDateFormat)

**목적**: 날짜가 지정된 형식과 일치하는지 확인하며, 디버깅을 위한 콘솔 로그 포함

**함수명**: `isCheckDateFormat`

**매개변수**:

- `date` (DateType): 확인할 날짜
- `format` (Format): 확인할 날짜 형식 문자열

**반환값**: 날짜 형식이 일치하면 true, 그렇지 않으면 false

**사용 예시**:

```typescript
import { isCheckDateFormat } from "@/utils/date";

// 날짜 형식이 일치하는지 확인
console.log(isCheckDateFormat("2023-12-25", "YYYY-MM-DD"));
// 출력: true

console.log(isCheckDateFormat("25/12/2023", "DD/MM/YYYY"));
// 출력: true

// 형식이 일치하지 않는 경우 (콘솔에 에러 메시지 출력)
console.log(isCheckDateFormat("2023-12-25", "DD/MM/YYYY"));
// 콘솔: ❌ date: "2023-12-25", format: "DD/MM/YYYY", 날짜 형식이 일치하지 않습니다.
// 출력: false

// 유효하지 않은 날짜
console.log(isCheckDateFormat(undefined, "YYYY-MM-DD"));
// 콘솔: ❌ date: "undefined", 날짜가 유효하지 않습니다.
// 출력: false
```

**키워드**: 날짜, 형식, 검증, format validation, 디버깅, 로그

---

## 4. 내일 날짜 생성 함수 (getTomorrowDate)

**목적**: 현재 날짜에서 하루를 더한 내일 날짜를 Date 객체로 반환

**함수명**: `getTomorrowDate`

**매개변수**: 없음

**반환값**: 내일 날짜의 Date 객체

**사용 예시**:

```typescript
import { getTomorrowDate } from "@/utils/date";

// 내일 날짜 가져오기
const tomorrow = getTomorrowDate();
console.log(tomorrow);
// 출력: Date 객체 (현재 날짜 + 1일)

// 다른 함수와 함께 사용
import { formatDate } from "@/utils/date";

const tomorrowFormatted = formatDate(getTomorrowDate(), "YYYY년 MM월 DD일");
console.log(tomorrowFormatted);
// 출력: '2024년 01월 16일' (현재가 2024년 1월 15일인 경우)
```

**키워드**: 날짜, 내일, 계산, date calculation, tomorrow

---

## 5. 폼 변경 필드 추출 함수 (getChangedFormFields)

**목적**: react-hook-form의 dirtyFields를 사용하여 변경된 필드만 추출하며, 중첩 객체와 배열도 재귀적으로 처리

**함수명**: `getChangedFormFields`

**매개변수**:

- `dirtyFields` (DirtyFields): react-hook-form에서 제공하는 변경된 필드 정보
- `formValues` (FormFieldValues): 현재 폼 데이터 값

**반환값**: 변경된 필드만 포함하는 객체 (ReturnChangedFields)

**사용 예시**:

```typescript
import { getChangedFormFields } from "@/utils/form";

// 기본 사용법
const dirtyFields = {
  name: true,
  email: true,
  age: false,
  profile: {
    bio: true,
    avatar: false,
  },
  hobbies: {
    0: { name: true },
    1: { name: false },
  },
};

const formValues = {
  name: "김철수",
  email: "kim@example.com",
  age: 30,
  profile: {
    bio: "안녕하세요",
    avatar: "avatar.jpg",
  },
  hobbies: [
    { id: "1", name: "독서" },
    { id: "2", name: "영화감상" },
  ],
};

const changedFields = getChangedFormFields(dirtyFields, formValues);
console.log(changedFields);
// 출력: {
//   name: "김철수",
//   email: "kim@example.com",
//   profile: {
//     bio: "안녕하세요"
//   },
//   hobbies: [
//     { id: "1", name: "독서" }
//   ]
// }

// 빈 폼 데이터 처리
const emptyResult = getChangedFormFields({}, {});
console.log(emptyResult);
// 콘솔: getChangedFormFields: 폼 데이터가 비어있습니다.
// 출력: {}

// 배열 요소의 id 자동 추가
const arrayDirtyFields = {
  items: {
    0: { name: true }, // id가 없는 변경된 항목
    1: { description: true },
  },
};

const arrayFormValues = {
  items: [
    { name: "새 항목" }, // id 없음
    { id: "existing-1", description: "기존 항목" }, // id 있음
  ],
};

const arrayResult = getChangedFormFields(arrayDirtyFields, arrayFormValues);
console.log(arrayResult);
// 출력: {
//   items: [
//     { name: "새 항목", id: "" },  // 빈 문자열로 id 추가
//     { id: "existing-1", description: "기존 항목" }  // 기존 id 유지
//   ]
// }
```

**키워드**: 폼, react-hook-form, dirtyFields, 변경감지, 중첩객체, form validation

---

## 6. 숫자 입력 변환 함수 (convertNumericInput)

**목적**: React input 요소에서 숫자만 입력받도록 변환하는 이벤트 핸들러 생성

**함수명**: `convertNumericInput`

**매개변수**:

- `onChange` (function): 숫자 값 변경 시 호출될 콜백 함수 `(value: string) => void`

**반환값**: React onChange 이벤트 핸들러 함수

**사용 예시**:

```typescript
import { convertNumericInput } from "@/utils/input";
import { useState } from "react";

// 컴포넌트에서 사용
const MyComponent = () => {
  const [numericValue, setNumericValue] = useState("");

  return (
    <input
      type="text"
      value={numericValue}
      onChange={convertNumericInput(setNumericValue)}
      placeholder="숫자만 입력 가능"
    />
  );
};

// 수동으로 테스트
const handleChange = convertNumericInput((value) => {
  console.log("숫자 값:", value);
});

// 가상의 이벤트 객체 (실제로는 React에서 전달)
const mockEvent = {
  target: { value: "abc123def456" },
} as React.ChangeEvent<HTMLInputElement>;

handleChange(mockEvent);
// 출력: "숫자 값: 123456"
```

**키워드**: 숫자입력, React, input, 숫자필터, numeric input, form control

---

## 7. 숫자 포맷팅 함수 (formatNumberToLocaleStringWithDecimals)

**목적**: 숫자를 지정된 소수점 자리수와 처리 방식으로 변환 후 한국 로케일 천단위 콤마 포함 문자열로 변환

**함수명**: `formatNumberToLocaleStringWithDecimals`

**매개변수**:

- `value` (number): 포맷팅할 숫자 값
- `decimalPlaces` (number, 기본값: 2): 소수점 자리수
- `mode` ('floor' | 'round' | 'ceil', 기본값: 'floor'): 소수점 처리 방식

**반환값**: 지정된 방식으로 처리되고 천단위 콤마가 포함된 문자열

**사용 예시**:

```typescript
import { formatNumberToLocaleStringWithDecimals } from "@/utils/input";

// 기본 사용법 (소수점 2자리, 버림 처리)
console.log(formatNumberToLocaleStringWithDecimals(1234.5678));
// 출력: "1,234.56"

// 소수점 3자리, 반올림 처리
console.log(formatNumberToLocaleStringWithDecimals(1234.5678, 3, "round"));
// 출력: "1,234.568"

// 소수점 1자리, 올림 처리
console.log(formatNumberToLocaleStringWithDecimals(1234.5678, 1, "ceil"));
// 출력: "1,234.6"

// 소수점 0자리 (정수만)
console.log(formatNumberToLocaleStringWithDecimals(1234.5678, 0));
// 출력: "1,234"

// 음수 처리
console.log(formatNumberToLocaleStringWithDecimals(-1234.5678, 2, "round"));
// 출력: "-1,234.57"
```

**키워드**: 숫자포맷팅, 소수점처리, 천단위콤마, 로케일, 반올림, 버림, 올림, number formatting

---

## 8. 콤마 문자열 숫자 변환 함수 (parseNumberFromCommas)

**목적**: 천단위 콤마가 포함된 문자열을 숫자로 변환

**함수명**: `parseNumberFromCommas`

**매개변수**:

- `value` (string): 천단위 콤마가 포함된 문자열

**반환값**: 숫자 값 또는 null (빈 값이거나 숫자로 변환 불가능한 경우)

**사용 예시**:

```typescript
import { parseNumberFromCommas } from "@/utils/input";

// 기본 사용법
console.log(parseNumberFromCommas("1,234,567"));
// 출력: 1234567

console.log(parseNumberFromCommas("1,234.56"));
// 출력: 1234.56

// 공백 제거 후 변환
console.log(parseNumberFromCommas("  1,234,567  "));
// 출력: 1234567

// 빈 문자열 처리
console.log(parseNumberFromCommas(""));
// 출력: null

console.log(parseNumberFromCommas("   "));
// 출력: null

// 숫자가 아닌 값 처리
console.log(parseNumberFromCommas("abc,def"));
// 출력: null

// 음수 처리
console.log(parseNumberFromCommas("-1,234.56"));
// 출력: -1234.56
```

**키워드**: 콤마제거, 문자열변환, 숫자파싱, parse number, comma removal

---

## 9. 소수점 버림 함수 (floorToTwoDecimals)

**목적**: 숫자를 소수점 둘째자리까지 버림 처리

**함수명**: `floorToTwoDecimals`

**매개변수**:

- `value` (number): 버림 처리할 숫자

**반환값**: 소수점 둘째자리까지 버림 처리된 숫자

**사용 예시**:

```typescript
import { floorToTwoDecimals } from "@/utils/input";

// 기본 사용법
console.log(floorToTwoDecimals(1234.5678));
// 출력: 1234.56

console.log(floorToTwoDecimals(9.999));
// 출력: 9.99

// 소수점이 2자리 미만인 경우
console.log(floorToTwoDecimals(1234.5));
// 출력: 1234.5

console.log(floorToTwoDecimals(1234));
// 출력: 1234

// 음수 처리 (더 작은 값으로 버림)
console.log(floorToTwoDecimals(-1234.5678));
// 출력: -1234.57 (음수에서 floor는 더 작은 값)

// 매우 작은 수
console.log(floorToTwoDecimals(0.999));
// 출력: 0.99
```

**키워드**: 소수점버림, 소수점처리, floor, 둘째자리, decimal truncation

---

## 10. 가격 포맷팅 함수 (formatDecimalPrice)

**목적**: 숫자를 한국 기준으로 포맷하며, 정수는 소수점 없이, 실수는 소수점 포함하여 표시

**함수명**: `formatDecimalPrice`

**매개변수**:

- `price` (number | string, 선택적): 포맷팅할 가격 값

**반환값**: 포맷팅된 가격 문자열, 값이 없으면 '-' 반환

**사용 예시**:

```typescript
import { formatDecimalPrice } from "@/utils/number";

// 정수 처리 (소수점 없이 표시)
console.log(formatDecimalPrice(3000));
// 출력: "3,000"

console.log(formatDecimalPrice(1234567));
// 출력: "1,234,567"

// 실수 처리 (소수점 포함하여 표시)
console.log(formatDecimalPrice(3000.5));
// 출력: "3,000.5"

console.log(formatDecimalPrice(1234.567));
// 출력: "1,234.567"

// 문자열로 전달된 숫자
console.log(formatDecimalPrice("3000"));
// 출력: "3,000"

console.log(formatDecimalPrice("3000.5"));
// 출력: "3,000.5"

// 빈 값 처리
console.log(formatDecimalPrice());
// 출력: "-"

console.log(formatDecimalPrice(null));
// 출력: "-"

console.log(formatDecimalPrice(undefined));
// 출력: "-"
```

**키워드**: 가격포맷팅, 한국로케일, 천단위콤마, 소수점표시, price formatting

---

## 11. 휴대폰 번호 포맷팅 함수 (formatPhoneNumber)

**목적**: 휴대폰 번호를 000-0000-0000 형식으로 포맷팅

**함수명**: `formatPhoneNumber`

**매개변수**:

- `phoneNumber` (string, 선택적): 포맷팅할 휴대폰 번호

**반환값**: 포맷팅된 휴대폰 번호 문자열, 값이 없으면 '-' 반환

**사용 예시**:

```typescript
import { formatPhoneNumber } from "@/utils/number";

// 기본 사용법
console.log(formatPhoneNumber("01012345678"));
// 출력: "010-1234-5678"

console.log(formatPhoneNumber("01987654321"));
// 출력: "019-8765-4321"

console.log(formatPhoneNumber("01112345678"));
// 출력: "011-1234-5678"

// 빈 값 처리
console.log(formatPhoneNumber());
// 출력: "-"

console.log(formatPhoneNumber(null));
// 출력: "-"

console.log(formatPhoneNumber(undefined));
// 출력: "-"

console.log(formatPhoneNumber(""));
// 출력: "-"
```

**키워드**: 휴대폰번호, 전화번호포맷팅, 하이픈추가, phone formatting

---

## 12. '전체' 값 변환 함수 (mapToUndefinedIfAll)

**목적**: 값이 '전체'인 경우 undefined로 변환, 그렇지 않으면 원래 값 반환

**함수명**: `mapToUndefinedIfAll`

**매개변수**:

- `value` (string | undefined): 변환할 문자열 값

**반환값**: '전체'인 경우 undefined, 그렇지 않으면 원래 값

**사용 예시**:

```typescript
import { mapToUndefinedIfAll } from "@/utils/transforms";

// '전체' 값 변환
console.log(mapToUndefinedIfAll("전체"));
// 출력: undefined

// 다른 값은 그대로 반환
console.log(mapToUndefinedIfAll("서울"));
// 출력: "서울"

console.log(mapToUndefinedIfAll("부산"));
// 출력: "부산"

// undefined는 그대로 반환
console.log(mapToUndefinedIfAll(undefined));
// 출력: undefined

// 빈 문자열은 그대로 반환
console.log(mapToUndefinedIfAll(""));
// 출력: ""
```

**키워드**: 전체값변환, undefined변환, 선택값처리, value transformation

---

## 13. 빈 문자열 변환 함수 (mapToUndefinedIfEmpty)

**목적**: 값이 빈 문자열인 경우 undefined로 변환, 그렇지 않으면 원래 값 반환

**함수명**: `mapToUndefinedIfEmpty`

**매개변수**:

- `value` (string | undefined): 변환할 문자열 값

**반환값**: 빈 문자열인 경우 undefined, 그렇지 않으면 원래 값

**사용 예시**:

```typescript
import { mapToUndefinedIfEmpty } from "@/utils/transforms";

// 빈 문자열 변환
console.log(mapToUndefinedIfEmpty(""));
// 출력: undefined

// 값이 있는 경우 그대로 반환
console.log(mapToUndefinedIfEmpty("hello"));
// 출력: "hello"

console.log(mapToUndefinedIfEmpty("0"));
// 출력: "0"

// undefined는 그대로 반환
console.log(mapToUndefinedIfEmpty(undefined));
// 출력: undefined

// 공백 문자열은 빈 문자열이 아니므로 그대로 반환
console.log(mapToUndefinedIfEmpty(" "));
// 출력: " "
```

**키워드**: 빈문자열변환, undefined변환, 빈값처리, empty string transformation

---

## 14. 빈 숫자 변환 함수 (mapToUndefinedIfEmptyNumber)

**목적**: 값이 0인 경우 undefined로 변환, 그렇지 않으면 원래 값 반환

**함수명**: `mapToUndefinedIfEmptyNumber`

**매개변수**:

- `value` (number | undefined): 변환할 숫자 값

**반환값**: 0인 경우 undefined, 그렇지 않으면 원래 값

**사용 예시**:

```typescript
import { mapToUndefinedIfEmptyNumber } from "@/utils/transforms";

// 0 값 변환
console.log(mapToUndefinedIfEmptyNumber(0));
// 출력: undefined

// 다른 숫자는 그대로 반환
console.log(mapToUndefinedIfEmptyNumber(1));
// 출력: 1

console.log(mapToUndefinedIfEmptyNumber(-1));
// 출력: -1

console.log(mapToUndefinedIfEmptyNumber(0.5));
// 출력: 0.5

// undefined는 그대로 반환
console.log(mapToUndefinedIfEmptyNumber(undefined));
// 출력: undefined
```

**키워드**: 빈숫자변환, 0값변환, undefined변환, number transformation

---

## 15. 숫자 파싱 함수 (parseNumberOrUndefined)

**목적**: 문자열 값을 숫자로 변환, 변환 불가능하거나 undefined인 경우 undefined 반환

**함수명**: `parseNumberOrUndefined`

**매개변수**:

- `value` (string | undefined): 변환할 문자열 값

**반환값**: 파싱된 숫자 또는 undefined

**사용 예시**:

```typescript
import { parseNumberOrUndefined } from "@/utils/transforms";

// 유효한 숫자 문자열 변환
console.log(parseNumberOrUndefined("123"));
// 출력: 123

console.log(parseNumberOrUndefined("0"));
// 출력: 0

console.log(parseNumberOrUndefined("-456"));
// 출력: -456

// 소수점이 있는 문자열 (parseInt 사용으로 정수만 반환)
console.log(parseNumberOrUndefined("123.45"));
// 출력: 123

// 변환 불가능한 문자열
console.log(parseNumberOrUndefined("abc"));
// 출력: undefined

console.log(parseNumberOrUndefined(""));
// 출력: undefined

// undefined 입력
console.log(parseNumberOrUndefined(undefined));
// 출력: undefined
```

**키워드**: 숫자파싱, 문자열변환, parseInt, number parsing

---

## 16. 불린 문자열 파싱 함수 (parseBooleanStringOrUndefined)

**목적**: 문자열을 boolean 값으로 변환, 'true'나 'false'가 아닌 경우 undefined 반환

**함수명**: `parseBooleanStringOrUndefined`

**매개변수**:

- `value` (string, 선택적): 변환할 문자열 값

**반환값**: boolean 값 또는 undefined

**사용 예시**:

```typescript
import { parseBooleanStringOrUndefined } from "@/utils/transforms";

// 'true' 문자열 변환
console.log(parseBooleanStringOrUndefined("true"));
// 출력: true

// 'false' 문자열 변환
console.log(parseBooleanStringOrUndefined("false"));
// 출력: false

// 다른 문자열들은 undefined 반환
console.log(parseBooleanStringOrUndefined("True"));
// 출력: undefined

console.log(parseBooleanStringOrUndefined("FALSE"));
// 출력: undefined

console.log(parseBooleanStringOrUndefined("1"));
// 출력: undefined

console.log(parseBooleanStringOrUndefined("0"));
// 출력: undefined

// undefined 입력
console.log(parseBooleanStringOrUndefined(undefined));
// 출력: undefined

console.log(parseBooleanStringOrUndefined(""));
// 출력: undefined
```

**키워드**: 불린파싱, 문자열변환, boolean parsing, true false

---

## 17. 빈 배열 변환 함수 (mapToUndefinedIfEmptyArray)

**목적**: 배열이 비어있는 경우 undefined로 변환, 그렇지 않으면 원래 값 반환

**함수명**: `mapToUndefinedIfEmptyArray`

**매개변수**:

- `value` (string[] | undefined): 변환할 문자열 배열

**반환값**: 빈 배열인 경우 undefined, 그렇지 않으면 원래 배열

**사용 예시**:

```typescript
import { mapToUndefinedIfEmptyArray } from "@/utils/transforms";

// 빈 배열 변환
console.log(mapToUndefinedIfEmptyArray([]));
// 출력: undefined

// 값이 있는 배열은 그대로 반환
console.log(mapToUndefinedIfEmptyArray(["apple", "banana"]));
// 출력: ["apple", "banana"]

console.log(mapToUndefinedIfEmptyArray(["single"]));
// 출력: ["single"]

// undefined는 그대로 반환
console.log(mapToUndefinedIfEmptyArray(undefined));
// 출력: undefined
```

**키워드**: 빈배열변환, undefined변환, 배열처리, empty array transformation

---

## 18. 시간을 분으로 변환 함수 (convertTimeToMinutes)

**목적**: HH:mm 형식의 시간 문자열을 분 단위 숫자로 변환

**함수명**: `convertTimeToMinutes`

**매개변수**:

- `timeString` (string | undefined): "HH:mm" 형식의 시간 문자열

**반환값**: 분 단위로 변환된 숫자, 잘못된 형식이면 undefined

**사용 예시**:

```typescript
import { convertTimeToMinutes } from "@/utils/transforms";

// 기본 사용법
console.log(convertTimeToMinutes("01:00"));
// 출력: 60

console.log(convertTimeToMinutes("02:30"));
// 출력: 150

console.log(convertTimeToMinutes("00:15"));
// 출력: 15

console.log(convertTimeToMinutes("24:00"));
// 출력: 1440

// 잘못된 형식
console.log(convertTimeToMinutes("1:00"));
// 출력: 60 (여전히 동작)

console.log(convertTimeToMinutes("abc:def"));
// 출력: undefined

console.log(convertTimeToMinutes("25:70"));
// 출력: 1570 (유효하지 않은 시간이지만 계산은 됨)

// undefined 입력
console.log(convertTimeToMinutes(undefined));
// 출력: undefined

console.log(convertTimeToMinutes(""));
// 출력: undefined
```

**키워드**: 시간변환, 분변환, 시간파싱, time to minutes

---

## 19. 분을 시간으로 변환 함수 (convertMinutesToTime)

**목적**: 분 단위 숫자를 HH:mm 형식의 시간 문자열로 변환

**함수명**: `convertMinutesToTime`

**매개변수**:

- `minutes` (string | undefined): 분 단위의 숫자 (문자열로 전달)

**반환값**: "HH:mm" 형식의 시간 문자열, 잘못된 입력이면 undefined

**사용 예시**:

```typescript
import { convertMinutesToTime } from "@/utils/transforms";

// 기본 사용법
console.log(convertMinutesToTime("60"));
// 출력: "01:00"

console.log(convertMinutesToTime("150"));
// 출력: "02:30"

console.log(convertMinutesToTime("15"));
// 출력: "00:15"

console.log(convertMinutesToTime("1440"));
// 출력: "24:00"

// 0분 처리
console.log(convertMinutesToTime("0"));
// 출력: "00:00"

// 음수는 undefined 반환
console.log(convertMinutesToTime("-60"));
// 출력: undefined

// 잘못된 입력
console.log(convertMinutesToTime("abc"));
// 출력: undefined

// undefined 입력
console.log(convertMinutesToTime(undefined));
// 출력: undefined

console.log(convertMinutesToTime(""));
// 출력: undefined
```

**키워드**: 분변환, 시간변환, 시간포맷팅, minutes to time

---

## 20. 숫자 입력 검증 함수 (validateNumericInput)

**목적**: zod를 사용하여 숫자 입력 필드의 검증 스키마 생성 (빈 값 불허, 숫자만 허용, 0보다 큰 값만 허용)

**함수명**: `validateNumericInput`

**매개변수**:

- `fieldName` (string): 검증할 필드의 이름 (에러 메시지에 사용)

**반환값**: zod 검증 스키마 객체

**사용 예시**:

```typescript
import { validateNumericInput } from "@/utils/validate";
import { z } from "zod";

// 기본 사용법 - 단일 필드 검증
const ageSchema = validateNumericInput("나이");

// 유효한 값들
console.log(ageSchema.parse("25")); // "25"
console.log(ageSchema.parse("1")); // "1"
console.log(ageSchema.parse("100")); // "100"

// 오류가 발생하는 값들
try {
  ageSchema.parse(""); // 오류: "나이을 입력해 주세요"
} catch (error) {
  console.log(error.issues[0].message);
}

try {
  ageSchema.parse("abc"); // 오류: "숫자만 입력해 주세요"
} catch (error) {
  console.log(error.issues[0].message);
}

try {
  ageSchema.parse("0"); // 오류: "0보다 커야 합니다"
} catch (error) {
  console.log(error.issues[0].message);
}

try {
  ageSchema.parse("000"); // 오류: "0보다 커야 합니다"
} catch (error) {
  console.log(error.issues[0].message);
}

// 폼 스키마에서 사용
const formSchema = z.object({
  age: validateNumericInput("나이"),
  price: validateNumericInput("가격"),
  quantity: validateNumericInput("수량"),
});

// 폼 데이터 검증
const formData = {
  age: "25",
  price: "1000",
  quantity: "5",
};

const validatedData = formSchema.parse(formData);
console.log(validatedData);
// 출력: { age: "25", price: "1000", quantity: "5" }
```

**키워드**: zod검증, 숫자검증, 폼검증, 입력검증, numeric validation, form validation

---

## 21. 팝업 창 중앙 배치 함수 (getWindowPopupCenter)

**목적**: 팝업 창을 화면 가운데에 띄우기 위한 window.open 옵션 문자열 생성

**함수명**: `getWindowPopupCenter`

**매개변수**:

- `params` (WindowPopupCenterParams): 팝업 창 설정 객체
  - `popupWidth` (number): 팝업 창의 너비
  - `popupHeight` (number): 팝업 창의 높이

**반환값**: window.open의 features 매개변수로 사용할 옵션 문자열

**사용 예시**:

```typescript
import { getWindowPopupCenter } from "@/utils/window";

// 기본 사용법
const popupOptions = getWindowPopupCenter({
  popupWidth: 600,
  popupHeight: 400,
});

console.log(popupOptions);
// 출력: "width=600,height=400,left=660,top=340" (화면 크기에 따라 left, top 값 변동)

// 팝업 창 띄우기
window.open("https://example.com", "popup", popupOptions);

// 다양한 크기의 팝업
const smallPopup = getWindowPopupCenter({
  popupWidth: 400,
  popupHeight: 300,
});

const largePopup = getWindowPopupCenter({
  popupWidth: 1000,
  popupHeight: 800,
});

// 소셜 로그인 팝업
const loginPopupOptions = getWindowPopupCenter({
  popupWidth: 500,
  popupHeight: 600,
});

const loginWindow = window.open(
  "/auth/google",
  "googleLogin",
  loginPopupOptions
);

// 듀얼 모니터 환경에서도 올바른 위치 계산
const dualScreenPopup = getWindowPopupCenter({
  popupWidth: 800,
  popupHeight: 600,
});

// 이미지 뷰어 팝업
const imageViewerOptions = getWindowPopupCenter({
  popupWidth: 1200,
  popupHeight: 900,
});

window.open("/image-viewer", "imageViewer", imageViewerOptions);
```

**키워드**: 팝업창, 중앙배치, window.open, 브라우저팝업, popup center, 구 ERP 팝업

---

## 타입 정의

### 날짜 관련 타입

```typescript
type DateType = string | number | Date | undefined | null;
type Format = string;
type Locale = "ko" | "en";
```

### 폼 관련 타입

```typescript
type FormFieldValues = Record<string, any>;
type DirtyFields = Record<string, any> | boolean;
type ArrayDirtyField = Record<string, any>;
type ObjectDirtyField = Record<string, any>;
type ReturnChangedFields = Partial<Record<string, FormFieldValues>> | undefined;
```

### 입력 관련 타입

```typescript
// React 관련 타입 (React import 필요)
type InputChangeHandler = (e: React.ChangeEvent<HTMLInputElement>) => void;
type NumericInputMode = "floor" | "round" | "ceil";
```

### 변환 관련 타입

```typescript
type TransformValue<T> = T | undefined;
type TimeString = string; // "HH:mm" 형식
type MinutesString = string; // 분 단위 숫자 문자열
```

### 윈도우 관련 타입

```typescript
type WindowPopupCenterParams = {
  popupWidth: number;
  popupHeight: number;
};
```

## 의존성

이 유틸 함수들은 다음 라이브러리를 사용합니다:

### 날짜 관련

- **dayjs**: 날짜 조작 및 포맷팅을 위한 경량 라이브러리
- **dayjs/locale/ko**: 한국어 로케일 지원

### 폼 관련

- **react-hook-form**: 폼 상태 관리 및 변경 감지 (선택사항, dirtyFields 타입 호환성을 위해)

### 검증 관련

- **zod**: 타입 안전한 스키마 검증 라이브러리

## 설치 방법

```bash
# 날짜 관련 함수를 위한 의존성
npm install dayjs

# 폼 관련 함수를 위한 의존성 (이미 사용 중인 경우)
npm install react-hook-form

# React (대부분의 프로젝트에서 이미 설치됨)
npm install react

# 검증 관련 함수를 위한 의존성
npm install zod

# 또는 yarn 사용
yarn add dayjs react-hook-form react zod
```
