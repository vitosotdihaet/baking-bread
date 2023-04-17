import Link from 'next/link';
import {
    ReactNode, memo,
} from 'react';
import {
    Additional,
    Mods,
    classNames,
} from 'shared/lib/classNames/classNames';
import { PolymorphicComponentPropWithRef } from 'shared/types/ui';
import { Loader } from '../Loader/Loader';
import cls from './Button.module.scss';

type ButtonVariant = 'primary' | 'secondary' | 'outlined' | 'accent' |'clear';
type ButtonRadius = 'xs' | 'sm' | 'md' | 'lg' | 'xl';
type ButtonPadding = 'smPadding' | 'mdPadding';
type ButtonSize = 'small' | 'medium' | 'large';
type ButtonContentAlign = 'left' | 'center' | 'right';

type ButtonProps<C extends React.ElementType> = PolymorphicComponentPropWithRef<
    C,
    {
        className?: string;
        variant?: ButtonVariant;
        children: React.ReactNode
        before?: ReactNode;
        after?: ReactNode;
        disabled?: boolean;
        active?: boolean;
        fullWidth?: boolean;
        uppercase?: boolean;
        radius?: ButtonRadius;
        padding?: ButtonPadding;
        size?: ButtonSize;
        loading?: boolean;
        alignContent?: ButtonContentAlign;
        noIndent?: boolean;
        href?: string;
        link?: boolean;
    }
>;
type ButtonComponent = <C extends React.ElementType = 'button'>(
    props: ButtonProps<C>
) => React.ReactElement | null;

export const Button: ButtonComponent = memo(<C extends React.ElementType = 'button'>(props: ButtonProps<C>) => {
    const {
        className,
        children,
        as,
        variant = 'primary',
        before,
        after,
        disabled = false,
        fullWidth = true,
        uppercase = false,
        radius = 'xl',
        padding = 'mdPadding',
        size = 'medium',
        alignContent = 'left',
        loading = false,
        noIndent = false,
        href,
        link,
        ...otherProps
    } = props;
    const Component = as || 'button';
    const isDisabled = disabled || loading;

    const additional: Additional = [
        className,
        cls[variant],
        cls[size],
        cls[radius],
        cls[alignContent],
        cls[padding],
    ];

    const mods: Mods = {
        [cls.disabled]: isDisabled,
        [cls.fullWidth]: fullWidth,
        [cls.uppercase]: uppercase,
        [cls.link]: href,
        [cls.noIndent]: noIndent,
    };

    if (as === 'a' && href) {
        return (
            <Link
                href={href}
                className={classNames(cls.Button, mods, additional)}
                disabled={isDisabled}
                {...otherProps}
            >
                {before && <span className={cls.before}>{before}</span>}
                {loading && <Loader className={cls.loader} size='xs' color='disabled' />}
                {children}
                {after && <span className={cls.after}>{after}</span>}
            </Link>
        );
    }

    return (
        <Component
            className={classNames(cls.Button, mods, additional)}
            type='button'
            disabled={isDisabled}
            {...otherProps}
        >
            {before && <span className={cls.before}>{before}</span>}
            {loading && <Loader className={cls.loader} size='xs' color='disabled' />}
            {children}
            {after && <span className={cls.after}>{after}</span>}
        </Component>
    );
});
