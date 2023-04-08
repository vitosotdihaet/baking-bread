import {
    ReactNode, memo,
} from 'react';
import {
    Additional,
    Mods,
    classNames,
} from 'shared/lib/classNames/classNames';
import { Loader } from '../Loader/Loader';
import cls from './Button.module.scss';

type ButtonVariant = 'primary' | 'secondary' | 'outlined' | 'accent' |'clear';
type ButtonRadius = 'xs' | 'sm' | 'md' | 'lg' | 'xl';
type ButtonSize = 'small' | 'medium' | 'large';
type ButtonContentAlign = 'left' | 'center' | 'right';

type PolymorphicRef<C extends React.ElementType> = React.ComponentPropsWithRef<C>['ref'];

type AsProp<C extends React.ElementType> = { as?: C; };

type PropsToOmit<C extends React.ElementType, P> = keyof (AsProp<C> & P);

type PolymorphicComponentProp<
    C extends React.ElementType,
    Props = {}
> = React.PropsWithChildren<Props & AsProp<C>> &
Omit<React.ComponentPropsWithoutRef<C>, PropsToOmit<C, Props>>;

type PolymorphicComponentPropWithRef<
    C extends React.ElementType,
    Props = {}
> = PolymorphicComponentProp<C, Props> & { ref?: PolymorphicRef<C> };

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
        size?: ButtonSize;
        loading?: boolean;
        alignContent?: ButtonContentAlign;
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
        size = 'medium',
        alignContent = 'left',
        loading = false,
        active = false,
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
    ];
    const mods: Mods = {
        [cls.disabled]: isDisabled,
        [cls.fullWidth]: fullWidth,
        [cls.uppercase]: uppercase,
        [cls.active]: active,
    };

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
