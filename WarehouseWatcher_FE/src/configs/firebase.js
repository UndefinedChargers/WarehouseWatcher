// Import necessary Firebase and Vue functions
import { initializeApp } from "firebase/app";
import { getAuth, onAuthStateChanged } from "firebase/auth";
import { getFirestore, doc, getDoc } from "firebase/firestore";
import { ref } from "vue";

// Firebase configuration
const firebaseConfig = {
    apiKey: import.meta.env.VITE_FIREBASE_API_KEY,
    authDomain: import.meta.env.VITE_FIREBASE_AUTH_DOMAIN,
    projectId: import.meta.env.VITE_FIREBASE_PROJECT_ID,
    storageBucket: import.meta.env.VITE_FIREBASE_STORAGE_BUCKET,
    messagingSenderId: import.meta.env.VITE_FIREBASE_MESSAGING_SENDER_ID,
    appId: import.meta.env.VITE_FIREBASE_APP_ID,
    measurementId: import.meta.env.VITE_FIREBASE_MEASUREMENT_ID
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore();

// Reactive user state
const user = ref(null);
const isAdmin = ref(false);

async function checkIfAdmin(user) {
    if (!user) return false;

    try {
        const userDoc = await getDoc(doc(db, "users", user.uid));
        return userDoc.exists(); 
    } catch (error) {
        console.error("Error checking admin status:", error);
        return false;
    }
}

onAuthStateChanged(auth, async (currentUser) => {
    user.value = currentUser; 
    isAdmin.value = currentUser ? await checkIfAdmin(currentUser) : false;
    console.log(user.value ? `Logged in as ${user.value.email}` : "No user logged in.");
    console.log(isAdmin.value ? "User is an admin" : "User is a regular user");
});

// Export reactive variables
export { auth, db, user, isAdmin };
