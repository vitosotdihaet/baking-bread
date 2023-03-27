export interface User {
    id: number;
    userId: number;
    title: string;
    completed: boolean;
}

export interface UserSchema {
    data: User[];
}
