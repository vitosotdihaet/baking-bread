import {
    getLoginData,
    getLoginPassword,
    getLoginUsername,
} from 'features/Auth/model/selectors/getLoginState';
import { loginByUsername } from 'features/Auth/model/services/loginByUsername/loginByUsername';
import { authActions, authReducer } from 'features/Auth/model/slice/authSlice';
import Link from 'next/link';
import { ChangeEvent, FC, useCallback } from 'react';
import { useSelector } from 'react-redux';
import { useAppDispatch } from 'shared/hooks/useAppDispatch/useAppDispatch';
import { classNames } from 'shared/lib/classNames/classNames';
import {
    DynamicModuleLoader,
    ReducersList,
} from 'shared/lib/components/DynamicModuleLoader/DynamicModuleLoader';
import { Button } from 'shared/ui/Button';
/* eslint-disable */
// import cls from './LoginForm.module.scss';

interface LoginFormProps {
    className?: string;
}

const reducers: ReducersList = {
    authState: authReducer,
};

export const LoginForm: FC<LoginFormProps> = (props) => {
    const { className } = props;
    const dispatch = useAppDispatch();
    const username = useSelector(getLoginUsername);
    const password = useSelector(getLoginPassword);
    const loginData = useSelector(getLoginData);

    const onChangeUsername = useCallback((e: ChangeEvent<HTMLInputElement>) => {
        dispatch(authActions.setUsername(e.target.value));
    }, [dispatch]);

    const onChangePassword = useCallback((e: ChangeEvent<HTMLInputElement>) => {
        dispatch(authActions.setPassword(e.target.value));
    }, [dispatch]);

    const onLoginClick = useCallback(async () => {
        try {
            await dispatch(loginByUsername({ username, password }));
        } catch (error) {
            console.log(error)
        }
    }, [dispatch, username, password]);

    return (
        <DynamicModuleLoader reducers={reducers}>
            <div className={classNames('', {}, [className])}>
                <div><input value={username} onChange={onChangeUsername} placeholder='username' /></div>
                <div><input value={password} onChange={onChangePassword} placeholder='password' /></div>
            </div>
            <Button onClick={onLoginClick}>Login</Button>
            <Link href='/'>Back</Link>
        </DynamicModuleLoader>
    );
};
