JavaScript에서 변수 호이스팅은 중요한 개념이며, 이때 `var`와 `let/const`는 서로 다르게 동작합니다.

# `var`의 호이스팅: undefined로 초기화
`var`로 선언된 변수는 호이스팅되며, 실행 컨텍스트가 생성될 때 해당 변수는 메모리의 최상단으로 끌어올려져 (hoisting) undefined로 초기화됩니다. 이는 변수 선언이 코드 어디에 있든 간에 자바스크립트 엔진이 실행 컨텍스트의 생성 단계에서 미리 메모리에 할당하고 `undefined` 값을 부여하기 때문입니다.
### 예시
```javascript
console.log(x); // undefined
var x = 5;
console.log(x); // 5
```
#### 실행 순서
1. 자바스크립트는 코드 실행 전 `var x`를 호이스팅하여 메모리에 등록하지만, 그 값은 할당되지 않고 `undefined`로 초기화됩니다.
2. 따라서 첫 번째 `console.log(x)`는 `undefined`를 출력합니다.
3. 이후 `x = 5`가 실행되면서 `x`에 5가 할당되고, 두 번째 `console.log(x)`에서는 5가 출력됩니다.

즉, 호이스팅으로 인해 `var`로 선언된 변수는 코드 상단에서 접근 가능하지만, 초기화되기 전까지는 `undefined`를 반환하게 됩니다.

# `let`과 `const`의 호이스팅과 일시적 사각지대(TDZ)
`let`과 `const`로 선언된 변수도 호이스팅되지만, `var`와는 다르게 즉시 초기화되지 않습니다. **일시적 사각지대(TDZ, Temporal Dead Zone)**는 변수가 선언되고 초기화될 때까지 해당 변수에 접근할 수 없는 구간을 의미합니다.

### 예시
```javascript
console.log(a); // ReferenceError: Cannot access 'a' before initialization
let a = 10;
```
일시적 사각지대(TDZ)란?
- **일시적 사각지대(TDZ)**는 변수가 선언되었지만 초기화되지 않은 상태를 의미합니다.
- `let`이나 `const`로 선언된 변수는 호이스팅 되지만, 해당 변수를 초기화하기 전까지는 접근할 수 없으며, `ReferenceError`가 발생합니다.
- 초기화된 후에는 정상적으로 사용할 수 있습니다.
#### 실행순서
1. 자바스크립트는 실행 전에 `let a`를 호이스팅하여 메모리에 등록합니다. 하지만 `var`처럼 즉시 `undefined`로 초기화되지 않고, 초기화될 때까지 TDZ 상태에 놓입니다.
2. TDZ에 있는 상태에서 변수를 참조하면 ReferenceError가 발생합니다.
3. `a = 10`이 실행된 이후에는 비로소 변수 `a`가 초기화되어 정상적으로 사용할 수 있습니다.
#### TDZ 예시
```javascript
console.log(b); // ReferenceError: Cannot access 'b' before initialization
let b = 20;
console.log(b); // 20
```
- 첫 번째 `console.log(b)`에서 ReferenceError가 발생한 이유는 변수 `b`가 메모리에는 할당되었지만, 초기화되지 않았기 때문입니다. 이 시점에서는 변수를 접근할 수 없으므로 **일시적 사각지대(TDZ)**에 놓여 있습니다.
- `let b = 20;`이 실행된 후에는 `b`가 20으로 초기화되므로, 이후의 `console.log(b)`에서는 정상적으로 20을 출력합니다.

# `var`와 `let/const`의 차이 요약
### `var`
- 선언과 동시에 undefined로 초기화됩니다.
- 코드 어디에서든 선언 전에 접근 가능하지만, 값이 할당되기 전에는 `undefined`입니다.
- 호이스팅은 발생하지만 초기화된 값은 `undefined`입니다.
### `let/const`
- 호이스팅은 발생하지만, 선언된 시점까지는 **일시적 사각지대(TDZ)**에 놓여서 초기화되기 전까지 변수에 접근할 수 없습니다.
- 초기화 전에는 ReferenceError가 발생합니다.
- `const`는 선언과 동시에 값을 할당해야 하며, 값은 변경할 수 없습니다.

# 정리
### `var`
- 호이스팅: 변수가 코드 최상단으로 끌어올려집니다.
- 초기화: 초기값은 undefined로 설정됩니다.
- 선언 전 접근 가능: 호이스팅으로 인해 변수 선언 전에 접근해도 `undefined` 값을 반환합니다.
### `let/const`
- 호이스팅: 변수는 코드 상단으로 끌어올려지지만, 초기화되지 않고 TDZ에 놓입니다.
- 초기화 전 접근 불가: 일시적 사각지대(TDZ)에서는 변수를 사용할 수 없으며, ReferenceError가 발생합니다.
- 초기화 후 사용 가능: 변수가 초기화된 이후에는 정상적으로 사용할 수 있습니다.
### 핵심 요점
- `var`: 선언과 초기화가 동시에 이루어지며, 초기값은 `undefined`
- `let/const`: 선언과 초기화가 분리되며, 초기화 전에는 일시적 사각지대(TDZ)로 인해 변수에 접근할 수 없음