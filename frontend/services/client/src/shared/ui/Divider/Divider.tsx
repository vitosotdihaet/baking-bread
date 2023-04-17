import { FC, memo } from 'react';
import { classNames } from 'shared/lib/classNames/classNames';
import cls from './Divider.module.scss';

interface DividerProps {
    className?: string;
}

export const Divider: FC<DividerProps> = memo((props: DividerProps) => {
    const { className } = props;

    return (
        <hr className={classNames(cls.Divider, {}, [className])} />
    );
});
