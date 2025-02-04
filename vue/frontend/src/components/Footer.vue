<script setup>
import { AkInstagramFill, AkFacebookFill, AkTwitterFill } from '@kalimahapps/vue-icons';

</script>
<template>
    <div class="footer-wrapper">
        <div class="footer-content">
            <div class="left">
                <p class="title">Etiam et id tincidunt faucibus mollis a sociis pretium fermentum quis magna faucibus
                    lacus.</p>
            </div>
            <div class="right">
                <div class="links">
                    <div class="top">
                        <p class="title">Marketplace</p>
                    </div>
                    <div class="bottom">
                        <a href="#">Home</a>
                        <a href="#">Activity</a>
                        <a href="#">Discover</a>
                        <a href="#">Learn more</a>
                    </div>
                </div>
                <div class="links">
                    <div class="top">
                        <p class="title">Company</p>
                    </div>
                    <div class="bottom">
                        <a href="#">About us</a>
                        <a href="#">Services</a>
                        <a href="#">Portfolio</a>
                    </div>
                </div>
                <div class="links">
                    <div class="top">
                        <p class="title">Contact</p>
                    </div>
                    <div class="bottom">
                        <a href="#">Facebook</a>
                        <a href="#">Instagram</a>
                        <a href="#">Twitter</a>
                        <a href="#">Email</a>
                    </div>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <div class="left">
                <a href="#">
                    <AkInstagramFill />
                </a>
                <a href="#">
                    <AkFacebookFill />
                </a>
                <a href="#">
                    <AkTwitterFill />
                </a>
            </div>
            <div class="right">
                <p>Copyright 2021 Gaslur</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "Footer"
};
</script>

<style lang='scss' scoped>
.footer-wrapper {
    .footer-content {
        @include flex(row, space-between, flex-start);
        border-bottom: 1px solid $gray;
        padding-bottom: 50px;
        margin-bottom: 50px;

        .title {
            font-size: 40px;
            line-height: 60px;
            padding-right: 100px;
        }

        .left {
            width: 40%;

            p {
                font-weight: 500;

            }
        }

        .right {
            @include flex(row, space-between, flex-start);
            width: 60%;

            .links {
                .top {
                    p {
                        font-weight: 400;
                        margin-bottom: 30px;
                    }
                }

                .bottom {
                    @include flex(column, center, flex-start, 30px);

                    a {
                        font-weight: 400;
                        font-size: 24px;
                        line-height: 36px;
                        color: $light-gray;
                    }
                }
            }
        }
    }

    .footer-bottom {
        @include flex(row, space-between, center);
        padding-bottom: 100px;

        .left {
            a {
                margin-right: 20px;

                svg {
                    font-size: 30px;
                }
            }
        }

        .right {
            p {
                font-size: 24px;
                line-height: 36px;
                font-weight: 400;
                color: $gray;
            }
        }
    }
}
</style>