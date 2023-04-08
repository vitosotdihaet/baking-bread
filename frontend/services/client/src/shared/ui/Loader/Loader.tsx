import {
    FC,
    HTMLAttributes,
    memo,
} from 'react';
import { Additional, classNames } from 'shared/lib/classNames/classNames';
import cls from './Loader.module.scss';

type LoaderSize = 'xs' | 'sm' | 'md' | 'lg' | 'xl';
type LoaderColor = 'primary' | 'secondary' | 'accent' | 'highlight' | 'disabled';

interface LoaderProps extends HTMLAttributes<HTMLDivElement> {
    className?: string;
    size?: LoaderSize;
    color?: LoaderColor;
}

export const Loader: FC<LoaderProps> = memo((props: LoaderProps) => {
    const {
        className,
        size = 'md',
        color = 'primary',
        ...otherProps
    } = props;

    const additional: Additional = [
        className,
        cls[size],
        cls[color],
    ];

    return (
        <div
            className={classNames(cls.loader, {}, additional)}
            {...otherProps}
        />
    );
});
