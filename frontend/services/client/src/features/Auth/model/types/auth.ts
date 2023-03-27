import { LoginData } from '../services/loginByUsername/loginByUsername';

export interface AuthSchema {
    username: string;
    password: string
    data?: LoginData
}
