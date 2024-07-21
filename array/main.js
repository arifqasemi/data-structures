// function validatePassword(password) {
//     // Check length
//     if (password.length < 8) {
//         return false;
//     }

//     // Regular expressions to check required characters
//     const hasUpperCase = /[A-Z]/.test(password);
//     const hasLowerCase = /[a-z]/.test(password);
//     const hasDigit = /\d/.test(password);
//     const hasSpecialChar = /[!@#$%^&*()-+]/.test(password);

//     // Ensure all conditions are met
//     if (hasUpperCase && hasLowerCase && hasDigit && hasSpecialChar) {
//         return true;
//     } else {
//         return false;
//     }
// }

// // Sample usage
// console.log(validatePassword("Aa1!aaaa")); // true
// console.log(validatePassword("Aa1")); // false
// console.log(validatePassword("aaaaaaa!")); // false
// console.log(validatePassword("AAAAAAA1")); // false
// console.log(validatePassword("Aa1!aaaa")); // true

// function commonSubstring(a, b) {
//     // Ensure both arrays have the same length
//     if (a.length !== b.length) {
//         throw new Error("Both arrays should have the same length");
//     }
    
//     // Function to determine if two strings have a common substring
//     function hasCommonSubstring(str1, str2) {
//         // Use a set to track characters in str1
//         let set = new Set();
//         for (let char of str1) {
//             set.add(char);
//         }
        
//         // Check if any character in str2 exists in the set
//         for (let char of str2) {
//             if (set.has(char)) {
//                 return true;
//             }
//         }
        
//         return false;
//     }

//     // Loop through arrays a and b
//     for (let i = 0; i < a.length; i++) {
//         if (hasCommonSubstring(a[i], b[i])) {
//             console.log("YES");
//         } else {
//             console.log("NO");
//         }
//     }
// }

// // Example usage:
// const a = ['ab', 'cd', 'ef'];
// const b = ['af', 'ee', 'ef'];
// commonSubstring(a, b);





function maxOfMinima(arr, k) {
    let n = arr.length;
    if (k > n) {
        throw new Error("Subarray length k cannot be greater than the length of the array");
    }

    // Initialize the maximum of minima
    let maxOfMin = -Infinity;

    // Loop to find minima of each subarray of length k
    for (let i = 0; i <= n - k; i++) {
        // Get the subarray from i to i+k
        let subArray = arr.slice(i, i + k);

        // Find the minimum in the subarray
        let minInSubArray = Math.min(...subArray);

        // Update the maximum of minima
        if (minInSubArray > maxOfMin) {
            maxOfMin = minInSubArray;
        }
    }

    return maxOfMin;
}

// Example usage:
let arr = [1, 2, 3, 4, 5];
let k = 2;
console.log(maxOfMinima(arr, k)); // Output: 4
