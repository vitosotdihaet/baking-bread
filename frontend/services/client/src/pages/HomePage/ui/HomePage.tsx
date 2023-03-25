import { FC } from 'react';
import { classNames } from 'shared/lib/classNames/classNames';
import Bread from 'shared/assets/icons/bread.svg';
import { Button } from 'shared/ui/Button';
import { useTranslation } from 'next-i18next';
import { useRouter } from 'next/router';
import Link from 'next/link';
// import cls from './HomePage.module.scss';

interface HomePageProps {
    className?: string;
}

const HomePage: FC<HomePageProps> = (props) => {
    const { className } = props;
    const { t, i18n } = useTranslation();
    const router = useRouter();

    return (
        <div className={classNames('', {}, [className])}>
            {t('HomePage')}
            <Link href='/cart'>{t('Go to cart')}</Link>
            <Bread style={{ fill: 'brown' }} />
        </div>
    );
};

export default HomePage;
