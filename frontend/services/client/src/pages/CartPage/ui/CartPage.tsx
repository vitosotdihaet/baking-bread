import { FC } from 'react';
import { classNames } from 'shared/lib/classNames/classNames';
import Bread from 'shared/assets/icons/bread.svg';
import { Button } from 'shared/ui/Button';
import { useTranslation } from 'next-i18next';
import { useRouter } from 'next/router';
import Link from 'next/link';

interface CartPageProps {
    className?: string;
}

const CartPage: FC<CartPageProps> = (props) => {
    const { className } = props;
    const { t, i18n } = useTranslation();
    const router = useRouter();

    return (
        <div className={classNames('', {}, [className])}>
            {t('HomePage')}
            {t('CartPage')}
            <Link href='/'>{t('Go back')}</Link>
            <Bread style={{ fill: 'brown' }} />
        </div>
    );
};

export default CartPage;
