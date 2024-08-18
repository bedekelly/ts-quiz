## Basic Types
What type is this? `5` -- It's a `number`.

What type is this? `"hello"` -- It's a `string`.

Is this a number? `"5"` -- No, it's a `string`.

Is this a number? `15` -- Yes.

Is this a number? `-1` -- Yes.

Is this a number? `0.5` -- Yes.

Is this a string? `""` -- Yes.

---
## Arrays (1)
What type is this? Don't worry about syntax for now. `[1, 2, 3]` -- It's an array of numbers.

What type is this? Don't worry about syntax for now. `["hello", "world"]` -- It's an array of strings.

What type is this? Don't worry about syntax for now. `["hello", 123, "world", 456]` -- It's an array of strings *and* numbers.

---

## Objects
What type is this? `{ a: 123 }` -- It's an object.

What type is this? `{ a: [1, 2, 3]}` -- It's an object.

What type is this? `{ a: ["hello", "world"], b: [4, 5, 6]}` -- It's an object.

What type is this? `{ a: { b: ["hello"]}, b: [1, 2, { c: "world" }]}` -- It's an object. (We see a problem emerging. Calling all of these "an object" is a bit too vague.)

---

## Objects and Keys
What keys does this object have? `{ a: 1, b: 2 }` -- The keys are `a` and `b`.

What keys does this object have? `{}` -- It doesn't have any keys.

What keys does this object have? `{ a: 1, b: { c: 3 }}` -- The keys are `a` and `b`. Look carefully: `c` is not a key of this object.

---

## Objects and Values
What type are the values of this object? `{ a: 1, b: 2 }` -- The values are of type `number`.

What type are the values of this object? `{ a: 'hello', b: 'world' }` -- The values are of type `string`.

What type are the values of this object? `{ a: 1, b: 'hello', c: 2, d: 'world' }` -- The values are of type `string` and `number`.

---

## Object Types
Is it true that this object `a` is of type `{ hello: string }`?
```
const a = {
    hello: 'world'
}
```
-- yes: the TypeScript compiler by default remembers *exactly* which keys are in an object, but the values are degraded to more generic types.

Is it true that this object `a` is of type `{ hello: string, myNumber: number }`?
```
const a = {
    hello: 'world',
    myNumber: 123
}
```
-- yes; again, the compiler remembers the keys `hello` and `myNumber` perfectly, but remembers the more generic types `string` and `number` for the values.

---

## Annotations
Is it true that this `a` is a number? ```const a = 5``` -- Yes, `a` here is a number.

Is it true that `a` is a number? `const a: number = 5` -- Yes. We often don't need to, but we can add a type annotation here.

Is it true that this `a` is *of type* `number`? `const a = 5` -- Yes. This is just a slightly more precise way of saying the same thing.

Is it true that this `a` is *of type* `number`? `const a: number = 5` -- Yes. This is just a slightly more precise way of saying the same thing.

Is it true that `a` is of *type* `5`? `const a: 5 = 5` -- Yes. We've instructed the compiler to be even more specific with what type it remembers for this value. Instead of remembering that this value is a generic number, it makes a note that this value is the literal number 5.

---

## Annotations (2)
Is it true that `a` is of *type* `10`? `const a = 10` -- No. Without that annotation, the TypeScript compiler doesn't assume we want the literal number. For most cases, it's enough to remember that it's a `number`.

Will this compile without errors? `const expects_string: string = 5` -- no, since `5` does not match the type of `string`. The compiler tells us `Type 'number' is not assignable to type 'string'`.

`my_number` is of type `number`. Will this compile without errors?
```const expects_five: 5 = my_number``` -- No. `expects_five` has a more specific type, and the compiler can't prove that `my_number` will meet the requirements of that type. It tells us `Type 'number' is not assignable to type '5'`. If the compiler allowed this, we'd be able to set `expects_five` to `4` in this situation, or `10,000` , or `-8.5`.

Is it true that `a` is of type `'hello'`? `const a: 'hello' = 'hello'` -- yes. We can make more specific types with strings too!

---

## Subtypes
Is the value `1` assignable to type `number`? -- yes, 1 is a value which matches `number`.

Is the value `"hello"` assignable to type `number`? -- no, `"hello"` is not a valid value for `number`.

Is the value `"hello"` assignable to type `number | string`? -- yes, `"hello"` is a valid value for `number | string`, because it's a valid value for `string`.

Is the value `123` assignable to type `number | string`? -- yes, `123` is a valid value for `number | string`, because it matches `number`.

Is it true that this `a` is of type `'hello' | 'world'`? `const a: 'hello' | 'world' = 'hello'` -- Yes.

Is it true that this `a` is of type `'hello' | 'world'`? `const a: 'hello' = 'hello'` -- No. The compiler only remembers what types it's told about, so `a` is of type `'hello'`.

---

## Subtypes (2)

Will this compile without errors?
```typescript
let a: string
const b: 'hello' = 'hello'
a = b;
```
-- Yes, the compiler allows *more specific* types to be assigned to variables with *less specific types*.

Will this compile without errors? 
```typescript
let a: 'hello' | 'world';
const b: 'hello' = 'hello';
a = b;
```
-- yes, the compiler allows *more specific* types to be assigned to variables with *less specific types*.

Will this compile without errors?
```typescript
function returnsHelloOrWorld(): 'hello' | 'world' {
    return 'hello';
}
let a: 'hello' = returnsHelloOrWorld()
```
-- no, the compiler will report `'hello' | 'world'` is not assignable to type `'hello'`. For all it knows, the returned value is `'world'`.

Will this compile without errors?
```typescript
function returnsHelloOrWorld() {
    return 'hello';
}
let a: 'hello' = returnsHelloOrWorld()
```
-- no. Without a return type annotation, the compiler infers that the function returns a `string`, and doesn't allow it to be assigned to a variable with a more specific type `'hello'`.

Will this compile without errors?
```typescript
function returnsHelloOrWorld(): 'hello' {
    return 'hello';
}
let a: 'hello' = returnsHelloOrWorld()
```
-- yes, the annotation tells the compiler that the function returns `'hello'`, so it can be assigned to the variable `a`.

Will this compile without errors?
```typescript
function returnsHelloOrWorld(): 'hello' {
    return 'world';
}
let a: 'hello' = returnsHelloOrWorld()
```
-- no, the compiler checks that the return value matches the annotation on a function.

---

## Arrays (2)
What type is this? `[1, 2, 3]` -- an array of numbers. In TypeScript we can write this as `Array<number>`.

What type is this? `["hello", "world"]` -- an array of strings. In TypeScript we can write this as `Array<string>`.

What type is this? `[1, "hello", 2, "world"]` -- an array of strings and numbers. In TypeScript we can write this as `Array<string | number>`.

What type is `list` here?
```typescript
const a: 'hello' = 'hello';
const b: 'world' = 'world;
const list = [a, b];
```
-- `list` is of type `Array<'hello' | 'world'>`.

Is `[1, 2, 3]` of type `number[]`? -- yes, `number[]` is another way of writing `Array<number>`.

Is `["hello", "world"]` of type `string[]` -- yes, `string[]` is another way of writing `Array<string>`.

Is `list` here of type `('hello' | 'world')[]`?
```typescript
const a: 'hello' = 'hello';
const b: 'world' = 'world;
const list = [a, b];
```
-- yes, `list` is of type `Array<'hello' | 'world'>`, which can also be written as `('hello' | 'world')[]`. Round brackets here are just used to group types together.

Is `Array<number>` the same type as `number[]`? -- yes, `Array<something>` and `something[]` are two ways of writing the same thing. They refer to exactly the same type.

Is there a value which can be an `Array<number>`, but not a `number[]`? -- no, because the two types are the same, they have exactly the same possible values.

---

## Promises
Is `Promise.resolve(15)` of type `Promise<number>`? -- yes, `Promise<number>` is a type which means a promise which *resolves to* a number.

What type is `a` here?
```typescript
async function f() {
	return 123;
}
const a = f();
```
-- `a` is a `Promise<number>`. Async functions return promises which resolve to the values they return. This has the same effect as writing `Promise.resolve(123)`.

What type is `a` here?
```typescript
async function f() {
	return Promise.resolve(123);
}
const a = f();
```
-- `a` is a `Promise<number>`. Nested promises get "flattened".

What type is `a`?
```typescript
const a = Promise.resolve(Promise.resolve(Promise.resolve(123)))
```
-- `a` is a `Promise<number>`. Nested promises get "flattened".

---

## Types with parameters
What type is `a`?
```typescript
const a = Promise.resolve([1, 2, 3]);
```
-- `a` is a `Promise<Array<number>>`. It's a promise *of* an array *of* numbers.

What type is `a` here?
```typescript
async function f() {
	return [1, 2, 3]
}
const a = f()
```
-- `a` is a `Promise<Array<number>>`. It's a promise *of* an array *of* numbers.

Is `Promise<Array<number>>` the same type as `Promise<number[]>`? -- yes, because `Array<number>` is the same type as `number[]`.

What type is `a`?
```typescript
const h: 'hello' = 'hello';
const a = Promise.resolve(h);
```
-- `a` is a `Promise<'hello'>`. It's a promise which resolves to a value of type `'hello'`.

Is `Promise.resolve("hello")` a `Promise<'hello'>`? -- no, by default the compiler will only infer strings as `string`, not anything more specific. `Promise.resolve("hello")` is a `Promise<string>`.

---

## Nested Arrays
What type is `a`?
```typescript
const a = [
	[1, 2, 3],
	[4, 5, 6]
];
```
-- `a` is of type `Array<Array<number>>`. It's an array of arrays of numbers.

Is `a` an `Array<Array<string>>`? 
```typescript
const a = [
	["hello", "world"]
]
```
-- yes, `a` is an `Array<Array<string>>`.

Is `a` a `string[][]`? 
```typescript
const a = [
	["hello", "world"]
]
```
-- yes, `a` is an `Array<Array<string>>`, which can also be written as `string[][]`.

What type is `a` here?
```typescript
async function f() {
	return [
		["hello", "world"]
	]
}
const a = f();
```
-- yes, `a` is a `Promise<string[][]>`, or alternatively a `Promise<Array<Array<string>>>`. It's a Promise which will resolve to a value of type `string[][]`.

---

## Aliases
Is `NumberAlias` a type alias for `number`?
```typescript
type NumberAlias = number
```
-- yes, `NumberAlias` is now a type alias for `number`.

Is `NewAlias` a type alias for `number`?
```typescript
type NewAlias = NumberAlias
```
-- yes, setting one alias for another will set the new alias to the original type.

Will this compile without errors?
```typescript
type NumberAlias = number
const a: NumberAlias = 123;
```
-- yes, `NumberAlias` is an alias for `number`, so this is the same as writing `const a: number = 123`.

Will this compile without errors?
```typescript
type NumberAlias = number
type NewAlias = NumberAlias
const a: NewAlias = 123;
```
-- yes, `NewAlias` is another alias for `number`, so this is the same as writing `const a: number = 123`.

Will this compile without errors?
```typescript
type NumberAlias = number
type NewAlias = NumberAlias
const a: NewAlias = 'hello';
```
-- no, `NewAlias` is another alias for `number`, so this is the same as writing `const a: number = 'hello'`.

Is there a value which matches `NumberAlias` which doesn't match `number`? -- no, `NumberAlias` is exactly the same type as `number`, so all the same values will match both of them.

---

## Aliases for types with parameters
What is type `Mystery` here?
```typescript
type A = number
type B = Array<A>
type Mystery = Promise<B> 
```
-- `Mystery` is an alias for `Promise<Array<number>>`, or equivalently `Promise<number[]>`. Aliases don't create any new types, they're just new names for existing ones that can save some typing.

What is type `Puzzle` here?
```typescript
type A = 'hello' | 'world'
type B = Array<Promise<A>>
type Puzzle = B | A
```
-- `Puzzle` is of type `Array<Promise<'hello' | 'world'>> | 'hello' | 'world'`. Aliases are replaced like-for-like with the types they refer to.

Does `'hello'` match the type `Puzzle` above? -- yes, `'hello'` is one of the possible values for type `Array<Promise<'hello' | 'world'>> | 'hello' | 'world'`.

Does `[ Promise.resolve('world') ]` match the type `Puzzle` above? -- yes, that's one of the possible values for type `Array<Promise<'hello' | 'world'>> | 'hello' | 'world'`.

Does this compile without errors?
```typescript
type A = Array<number>
type B = Promise<string>
const a: A | B = [ Promise.resolve('123') ]; 
```
-- no, `[ Promise.resolve('123') ]` is of type `Array<Promise<string>>`, which isn't assignable to either `Array<number>` or `Promise<string>`, so therefore isn't assignable to `Array<number> | Promise<string>`, which is written here with aliases as `A | B`.

---

## Aliases with parameters
What is type `Mystery` here?
```typescript
type MakeArray<T> = Array<T>
type Mystery = MakeArray<number>
```
-- `Mystery` is the type `Array<number>`.

What is type `Puzzle` here?
```typescript
type MakePromise<TypeParameter> = Promise<TypeParameter>
type Puzzle = MakePromise<number>
```
-- `Puzzle` is a `Promise<number>`. The type `number` is passed to the parameter `TypeParameter`.

In `type MyType<MyParam> = ...`, is `MyParam` a type parameter? -- yes.

In `type MyType<OneParam, AnotherParam> = ...`, how many type parameters are there?  -- two: `OneParam` and `AnotherParam`.

In `type A<T> = ...`, is `A` a parameterised type? -- yes, because it has a parameter `T`, `A` is a parameterised type.

---

## Aliases for types with parameters (2)
What is type `A` here?
```typescript
type SomeType<ParamOne, ParamTwo> = Array<ParamOne | ParamTwo>;
type A = SomeType<number, string>
```
-- type `A` is `Array<number | string>`. `number` is passed in as `ParamOne`, and `string` is passed as `ParamTwo`.

Do type parameters need to be a single character? -- no, as in the examples above, type names can be any number of characters.

Does this compile without errors?
```typescript
type SomeType<ParamOne, ParamTwo> = Array<ParamOne | ParamTwo>;
type A = SomeType<number, string>
const a: A = [1, 2, "hello"]
```
-- yes, `a` is an `Array<string | number>`, so it matches the type referenced by the alias `A`.

Does this compile without errors?
```typescript
type SomeType<ParamOne, ParamTwo> = Array<ParamOne | ParamTwo>;
type A = SomeType<number, string>
const a: A = [1, 2, 3]
```
-- yes, `a` is a `number[]`, so it matches the type referenced by the alias `A`.

